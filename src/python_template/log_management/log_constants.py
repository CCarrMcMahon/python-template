import logging
from enum import Enum


class LogLevel(Enum):
    """Enumeration class representing different logging levels.

    This enumeration maps to standard Python logging levels, providing a type-safe way to specify
    log severity.

    Attributes:
        DEBUG (int): Detailed information for debugging (10).
        INFO (int): General information about program execution (20).
        WARNING (int): Indicates a potential problem (30).
        ERROR (int): Error that prevented function from working (40).
        CRITICAL (int): Critical error that prevents program from running (50).
    """

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class LogFormat(Enum):
    """Enumeration of predefined logging formats with increasing detail levels.

    This enumeration provides a set of predefined logging formats that can be used to configure the
    logging module with different levels of detail. The formats are designed to be used with the
    `logging.basicConfig` or `logging.Formatter` functions.

    Attributes:
        MINIMAL (str): The simplest logging format with only the log level and message.
        TIME_ONLY (str): Expands upon the minimal format by adding a timestamp.
        PRECISE_TIME (str): Adjusts the time format to include milliseconds.
        WITH_LOGGER (str): Adds the name of the logger in the output.
        WITH_FILENAME (str): Includes the filename where the log message originated.
        DETAILED (str): The most detailed logging format which adds the function name and line number.
    """

    MINIMAL = "%(levelname)-8s %(message)s"
    TIME_ONLY = "%(asctime)s %(levelname)-8s %(message)s"
    PRECISE_TIME = "%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s"
    WITH_LOGGER = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)-15s %(message)s"
    WITH_FILENAME = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)-15s [%(filename)s] %(message)s"
    DETAILED = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)-15s [%(filename)s@%(funcName)s:%(lineno)d] %(message)s"
