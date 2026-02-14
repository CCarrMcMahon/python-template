import logging
from datetime import datetime
from pathlib import Path
from typing import Any

from colorama import Fore, Style
from colorama import init as colorama_init

DATE_FORMAT = "%m/%d/%y"
TIME_FORMAT = "%H:%M:%S"
LOGS_DIR = "logs"
LOG_FILENAME_DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S"
LATEST_LOG_FILENAME = "latest.log"
LEVEL_COLOR = {
    "DEBUG": Fore.MAGENTA,
    "INFO": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Style.BRIGHT + Fore.RED,
}


class CustomFormatter(logging.Formatter):
    is_date_visible: bool
    is_timestamp_visible: bool
    is_milliseconds_visible: bool
    is_name_visible: bool
    use_short_name: bool
    use_colored_logging: bool

    def __init__(
        self,
        is_date_visible: bool = False,
        is_timestamp_visible: bool = True,
        is_milliseconds_visible: bool = True,
        is_name_visible: bool = True,
        use_short_name: bool = True,
        use_colored_logging: bool = True,
    ) -> None:
        self.is_date_visible = is_date_visible
        self.is_timestamp_visible = is_timestamp_visible
        self.is_milliseconds_visible = is_milliseconds_visible
        self.is_name_visible = is_name_visible
        self.use_short_name = use_short_name
        self.use_colored_logging = use_colored_logging

        colorama_init(autoreset=True)
        super().__init__()

    def format_date(self, current_datetime: datetime) -> str:
        if not self.is_date_visible:
            return ""

        date_str = current_datetime.strftime(DATE_FORMAT)
        if not self.use_colored_logging:
            return date_str

        return f"{Fore.GREEN}{date_str}{Style.RESET_ALL}"

    def format_timestamp(self, current_datetime: datetime) -> str:
        if not self.is_timestamp_visible:
            return ""

        timestamp_str = current_datetime.strftime(TIME_FORMAT)
        if self.is_milliseconds_visible:
            timestamp_str += f".{current_datetime.microsecond // 1000:03d}"

        if not self.use_colored_logging:
            return timestamp_str

        return f"{Fore.BLUE}{timestamp_str}{Style.RESET_ALL}"

    def format_levelname(self, levelname: str) -> str:
        levelname_str = f"{levelname:<9}"
        if not self.use_colored_logging:
            return levelname_str

        color = LEVEL_COLOR.get(levelname, Fore.WHITE)
        return f"{color}{levelname_str}{Style.RESET_ALL}"

    def format_name(self, name: str) -> str:
        if not self.is_name_visible:
            return ""

        name_str = name
        if self.use_short_name:
            name_str = name.split(".")[-1]

        if not self.use_colored_logging:
            return name_str

        return f"{Fore.CYAN}{name_str}{Style.RESET_ALL}"

    def format(self, record: logging.LogRecord) -> str:
        current_datetime = datetime.fromtimestamp(record.created).astimezone()

        date_str = self.format_date(current_datetime)
        timestamp_str = self.format_timestamp(current_datetime)
        levelname_str = self.format_levelname(record.levelname)
        name_str = self.format_name(record.name)
        msg_str = record.getMessage()

        log_parts = [date_str, timestamp_str, levelname_str, name_str, msg_str]
        log_str = " ".join(part for part in log_parts if part != "")

        # Avoid resetting style if not using colors to avoid displaying reset codes in log files
        if not self.use_colored_logging:
            return log_str

        # Prefix and suffix resets to ensure messages don't inherit colors
        return f"{Style.RESET_ALL}{log_str}{Style.RESET_ALL}"

    def formatException(self, ei: Any) -> str:
        exception_str = super().formatException(ei)

        # Avoid resetting style if not using colors to avoid displaying reset codes in log files
        if not self.use_colored_logging:
            return exception_str

        # Prefix and suffix resets to ensure tracebacks don't inherit colors
        return f"{Style.RESET_ALL}{exception_str}{Style.RESET_ALL}"


def init_terminal_logging(
    level: int = logging.INFO,
    *,
    is_date_visible: bool = False,
    is_timestamp_visible: bool = True,
    is_milliseconds_visible: bool = True,
    is_name_visible: bool = True,
    use_short_name: bool = True,
    use_colored_logging: bool = True,
) -> None:
    # Set root logger level to DEBUG to allow all messages through
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # Create stream handler if none exists
    stream_handler: logging.Handler | None = None
    for handler in root_logger.handlers:
        if isinstance(handler, logging.FileHandler):
            continue

        if isinstance(handler, logging.StreamHandler):
            stream_handler = handler
            break

    if stream_handler is None:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        root_logger.addHandler(stream_handler)

    # Prevent colored logging if not supported
    if use_colored_logging:
        if hasattr(stream_handler.stream, "isatty") and not stream_handler.stream.isatty():
            use_colored_logging = False

    stream_log_formatter = CustomFormatter(
        is_date_visible=is_date_visible,
        is_timestamp_visible=is_timestamp_visible,
        is_milliseconds_visible=is_milliseconds_visible,
        is_name_visible=is_name_visible,
        use_short_name=use_short_name,
        use_colored_logging=use_colored_logging,
    )

    stream_handler.setFormatter(stream_log_formatter)


def init_file_logging(
    logs_dir: str | Path | None = None,
    level: int = logging.DEBUG,
    *,
    is_date_visible: bool = True,
    is_timestamp_visible: bool = True,
    is_milliseconds_visible: bool = True,
    is_name_visible: bool = True,
    use_short_name: bool = False,
) -> Path:
    if logs_dir is None:
        logs_dir = Path.cwd() / LOGS_DIR

    logs_dir = Path(logs_dir)
    logs_dir.mkdir(parents=True, exist_ok=True)

    # Create timestamped log file path
    current_datetime = datetime.now().astimezone()
    datetime_str = current_datetime.strftime(LOG_FILENAME_DATETIME_FORMAT)
    milliseconds_str = f"{current_datetime.microsecond // 1000:03d}"
    log_file_path = logs_dir / f"{datetime_str}_{milliseconds_str}.log"

    # Create latest log file path
    latest_log_path = Path.cwd() / LATEST_LOG_FILENAME

    # Attach to root logger
    root_logger = logging.getLogger()
    file_log_formatter = CustomFormatter(
        is_date_visible=is_date_visible,
        is_timestamp_visible=is_timestamp_visible,
        is_milliseconds_visible=is_milliseconds_visible,
        is_name_visible=is_name_visible,
        use_short_name=use_short_name,
        use_colored_logging=False,
    )

    # Timestamped log file in logging directory
    timestamped_file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
    timestamped_file_handler.setLevel(level)
    timestamped_file_handler.setFormatter(file_log_formatter)
    root_logger.addHandler(timestamped_file_handler)

    # Latest log file in project root
    latest_file_handler = logging.FileHandler(latest_log_path, mode="w", encoding="utf-8")
    latest_file_handler.setLevel(level)
    latest_file_handler.setFormatter(file_log_formatter)
    root_logger.addHandler(latest_file_handler)

    return logs_dir


def initialize_logging(verbose: bool = False, noisy_loggers: list[str] | None = None) -> None:
    """Initialize terminal and file logging with appropriate log levels.

    This function sets up logging to the terminal and to log files, adjusting the log level based on
    the verbosity flag. It also suppresses overly verbose loggers.

    Args:
        verbose (bool): If True, set the terminal log level to DEBUG; otherwise, INFO.
        noisy_loggers (list[str] | None): List of logger names to suppress to WARNING level.
    """
    if noisy_loggers is None:
        noisy_loggers = []

    level = logging.DEBUG if verbose else logging.INFO
    init_terminal_logging(level=level)
    init_file_logging()

    for name in noisy_loggers:
        logging.getLogger(name).setLevel(logging.WARNING)
