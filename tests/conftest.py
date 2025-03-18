import logging

import pytest

from python_template.log_management.log_constants import LogFormat, LogLevel


def pytest_addoption(parser: pytest.Parser) -> None:
    """A pytest hook for adding custom arguments to pytest.

    Args:
        parser (pytest.Parser): The pytest parser object
    """
    # Optional arguments
    parser.addoption(
        "--log_level",
        type=str,
        choices=[level.name for level in LogLevel],
        help="The logging level to use for the root logger.",
    )
    parser.addoption(
        "--log_format",
        type=str,
        choices=[format.name for format in LogFormat],
        help="The logging format to use for the root logger.",
    )


def pytest_configure(config: pytest.Config) -> None:
    """A pytest hook for configuring the pytest session.

    Args:
        config (pytest.Config): The pytest config object
    """
    # Verbose mode will override all other logging settings
    if bool(config.getoption("verbose")):
        config.option.log_level = LogLevel.DEBUG.value
        config.option.log_format = LogFormat.LINE.value
        return

    # Command line arguments take precedence over configuration file settings
    log_level_opt: str | None = config.getoption("log_level")
    if log_level_opt is None:
        log_level_opt = config.getini("log_level")

    log_format_opt: str | None = config.getoption("log_format")
    if log_format_opt is None:
        log_format_opt = config.getini("log_format")

    # Update the logging level and format if the options are valid
    log_level = LogLevel.INFO.value
    if log_level_opt in LogLevel.__members__:
        log_level = LogLevel[log_level_opt].value

    log_format = LogFormat.MSECS.value
    if log_format_opt in LogFormat.__members__:
        log_format = LogFormat[log_format_opt].value

    # Overwrite the pytest configuration with our custom logging settings
    config.option.log_level = log_level
    config.option.log_format = log_format


@pytest.fixture(scope="function", autouse=True)
def example_function_fixture(request: pytest.FixtureRequest):
    logger = logging.getLogger(__name__)
    test_name = str(request.node.name)
    logger.debug("Starting test: %s", test_name)
    yield
    logger.debug("Ending test: %s", test_name)
