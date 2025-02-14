import logging

import pytest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def pytest_addoption(parser: pytest.Parser) -> None:
    """A pytest hook for adding custom arguments to pytest.

    Args:
        parser (pytest.Parser): The pytest parser object
    """
    parser.addoption(
        "--name",
        type=str,
        help="An example string argument for your name.",
    )


@pytest.fixture(scope="session", autouse=True)
def example_session_fixture():
    """An example pytest session level fixture that always runs to log a message when testing starts and ends."""
    logger.info("Started the testing session.")
    yield
    logger.info("Ended the testing session.")


@pytest.fixture(scope="function", autouse=True)
def example_function_fixture(request: pytest.FixtureRequest):
    """An example pytest function level fixture that always runs to log a message when a test starts and ends.

    Args:
        request (pytest.FixtureRequest): The pytest fixture request object
    """
    test_name = request.node.name
    logger.info('Started the test: "%s".', test_name)
    yield
    logger.info('Ended the test: "%s".', test_name)
