from enum import Enum


class LogLevel(Enum):
    """Enumeration class representing different logging levels.

    This enumeration maps to standard Python logging levels, providing a type-safe way to specify log severity.

    Attributes:
        DEBUG (str): Detailed information for debugging (10).
        INFO (str): General information about program execution (20).
        WARNING (str): Indicates a potential problem (30).
        ERROR (str): Error that prevented function from working (40).
        CRITICAL (str): Critical error that prevents program from running (50).
    """

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class LogFormat(Enum):
    """Enumeration of predefined logging formats with increasing detail levels.

    This enumeration provides a set of predefined logging formats that can be used to configure the logging module with
    different levels of detail. The formats are designed to be used with the `logging.basicConfig` or
    `logging.Formatter` functions.

    Attributes:
        SIMPLE (str): The simplest logging format with only the log level and message.
        TIME (str): Expands upon the minimal format by adding a timestamp.
        MSECS (str): Adjusts the time format to include milliseconds.
        NAME (str): Adds the name of the logger to the output.
        FILENAME (str): Includes the filename where the log message originated.
        LINE (str): The most detailed logging format which adds the line number and function name.
    """

    SIMPLE = "%(levelname)-8s %(message)s"
    TIME = "%(asctime)s %(levelname)-8s %(message)s"
    MSECS = "%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s"
    NAME = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)s %(message)s"
    FILENAME = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)s [%(filename)s] %(message)s"
    LINE = "%(asctime)s.%(msecs)03d %(levelname)-8s %(name)s [%(filename)s:%(lineno)d @%(funcName)s(...)] %(message)s"
