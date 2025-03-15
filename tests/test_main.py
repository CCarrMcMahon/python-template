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
    log_level = LogLevel[request.config.getoption("log_level")]

    # Check the logging output
    if log_level == LogLevel.DEBUG:
        record = caplog.records[-2]
        assert record.message == "Debug logging enabled."
        assert record.levelname == "DEBUG"
    if log_level == LogLevel.DEBUG or log_level == LogLevel.INFO:
        record = caplog.records[-1]
        assert record.message == "Hello, World!"
        assert record.levelname == "INFO"
