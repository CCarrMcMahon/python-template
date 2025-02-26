import logging
from collections.abc import Mapping
from typing import Any, Literal

from python_template.log_management.log_constants import LogFormat, LogLevel


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


def initialize_root_logger(log_level: LogLevel, log_format: LogFormat) -> None:
    """Initialize the root logger with the provided log level and format.

    Args:
        log_level (LogLevel): The logging level to use for the root logger.
        log_format (LogFormat): The logging format to use for the root logger.
    """
    # Check if the root logger has already been configured
    root_logger = logging.getLogger()
    if len(root_logger.handlers) != 0:
        return

    # Create a new handler for the root logger
    handler = logging.StreamHandler()

    # Apply the log level and format to the handler
    formatter = ShortNameFormatter(log_format.value)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(log_level.value)
