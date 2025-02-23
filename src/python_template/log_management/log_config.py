import logging
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Literal

from python_template.log_management.log_constants import LogFormat, LogLevel, LogVerbosity


@dataclass
class VerbosityConfig:
    """A dataclass to hold the logging level and format for a given verbosity level."""

    log_level: LogLevel
    log_format: LogFormat


LOGGING_CONFIGS = {
    LogVerbosity.SIMPLE: VerbosityConfig(log_level=LogLevel.INFO, log_format=LogFormat.BASIC),
    LogVerbosity.NORMAL: VerbosityConfig(log_level=LogLevel.INFO, log_format=LogFormat.TIMESTAMPED),
    LogVerbosity.DEBUG: VerbosityConfig(log_level=LogLevel.DEBUG, log_format=LogFormat.FILE_NAME),
    LogVerbosity.VERBOSE: VerbosityConfig(log_level=LogLevel.DEBUG, log_format=LogFormat.FILE_LINE),
}


class ShortNameFormatter(logging.Formatter):
    """A custom logging formatter that only displays the short name of the logger."""

    def __init__(
        self,
        fmt: str | None = None,
        datefmt: str | None = "%m/%d/%Y %H:%M:%S",
        style: Literal["%", "{", "$"] = "%",
        validate: bool = True,
        *,
        defaults: Mapping[str, Any] | None = None,
    ):
        """Initialize the ShortNameFormatter with the provided format and date format.

        Args:
            fmt (str | None): The format string for the log message.
            datefmt (str | None): The date format string for the log message.
            style (Literal["%", "{", "$"]): The style of the format string.
            validate (bool): Whether or not to validate the format string.
            defaults (Mapping[str, Any] | None): The default values for the format string.
        """
        super().__init__(fmt, datefmt, style, validate, defaults=defaults)

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record with only the short name of the logger.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            message (str): The formatted log message.
        """
        record.name = record.name.split(".")[-1]
        return super().format(record)


def setup_root_logger(verbosity: LogVerbosity = LogVerbosity.NORMAL) -> None:
    """Set up the root logger with the provided verbosity level.

    Args:
        verbosity (LogVerbosity): The verbosity level to set the logger to.
    """
    # Check if the root logger already has handlers
    root_logger = logging.getLogger()
    if len(root_logger.handlers) != 0:
        return

    # Create a new handler for the root logger
    handler = logging.StreamHandler()

    # Set the log level and format based on the verbosity
    logging_config = LOGGING_CONFIGS.get(verbosity)

    # Apply the log level and format to the handler
    formatter = ShortNameFormatter(logging_config.log_format.value)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging_config.log_level.value)
