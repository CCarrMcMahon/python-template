import logging

import pytest

from python_template import main
from python_template.log_management.log_constants import LogLevel

logger = logging.getLogger(__name__)


def test_log_intro(request: pytest.FixtureRequest, caplog: pytest.LogCaptureFixture) -> None:
    """Tests the log_intro function.

    Args:
        request (pytest.FixtureRequest): The pytest fixture request object.
        caplog (pytest.LogCaptureFixture): The pytest log capture fixture.
    """
    # Run the logging intro function
    main.log_intro()

    # Get the logging configuration
    log_level = LogLevel[request.config.getoption("log_lvl").upper()]
    verbose = request.config.getoption("log_v")
    if verbose:
        log_level = LogLevel.DEBUG

    # Check the logging output
    if log_level == LogLevel.DEBUG:
        assert caplog.records[-2].message == "Debug logging enabled."
    assert caplog.records[-1].message == "Hello, World!"

    # Check the logging format
    if log_level == LogLevel.DEBUG:
        assert caplog.records[-2].levelname == "DEBUG"
    assert caplog.records[-1].levelname == "INFO"

    logger.debug("Test complete.")
