import logging

import pytest

from python_template.log_management.log_config import initialize_root_logger
from python_template.log_management.log_constants import LogFormat, LogLevel


def pytest_addoption(parser: pytest.Parser) -> None:
    """A pytest hook for adding custom arguments to pytest.

    Args:
        parser (pytest.Parser): The pytest parser object
    """
    # Optional arguments
    parser.addoption(
        "--log_lvl",
        type=str,
        default=LogLevel.INFO.name.lower(),
        choices=[level.name.lower() for level in LogLevel],
        help="The logging level to use for the root logger.",
    )
    parser.addoption(
        "--log_fmt",
        type=str,
        default=LogFormat.MSECS.name.lower(),
        choices=[format.name.lower() for format in LogFormat],
        help="The logging format to use for the root logger.",
    )
    parser.addoption(
        "--log_v",
        action="store_true",
        help="Increase the verbosity of the logging output to include more detailed information.",
    )


@pytest.fixture(scope="session", autouse=True)
def example_session_fixture(pytestconfig: pytest.Config):
    log_lvl = LogLevel[pytestconfig.getoption("log_lvl").upper()]
    log_fmt = LogFormat[pytestconfig.getoption("log_fmt").upper()]
    log_v = bool(pytestconfig.getoption("log_v"))

    if log_v:
        log_lvl = LogLevel.DEBUG
        log_fmt = LogFormat.LINE

    initialize_root_logger(log_lvl, log_fmt)

    logger = logging.getLogger(__name__)
    logger.debug("Debug logging enabled.")
    logger.info("Starting the test session.")
    yield
    logger.info("Ending the test session.")
    logger.debug("Debug logging disabled.")


@pytest.fixture(scope="function", autouse=True)
def example_function_fixture(request: pytest.FixtureRequest):
    logger = logging.getLogger(__name__)
    test_name = str(request.node.name)
    logger.info("Starting test: %s", test_name)
    yield
    logger.info("Ending test: %s", test_name)
