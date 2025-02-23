import logging
from enum import Enum, auto


class LogLevel(Enum):
    """A copy of the logging levels provided by the logging module."""

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class LogFormat(Enum):
    """Common logging message formats."""

    BASIC = "%(levelname)-8s %(message)s"
    TIMESTAMPED = "%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s"
    LOGGER_NAME = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)s - %(message)s"
    FILE_NAME = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)s[%(filename)s] - %(message)s"
    FILE_FUNC = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)s[%(filename)s@%(funcName)s] - %(message)s"
    FILE_LINE = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)s[%(filename)s:%(lineno)d] - %(message)s"


class LogVerbosity(Enum):
    """Represents combinations of logging levels and formats."""

    SIMPLE = auto()
    NORMAL = auto()
    DEBUG = auto()
    VERBOSE = auto()
