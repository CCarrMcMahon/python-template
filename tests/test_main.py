import logging

import pytest

from python_template import main

logger = logging.getLogger(__name__)


def test_log_introduction(request: pytest.FixtureRequest, caplog: pytest.LogCaptureFixture) -> None:
    """Tests the log_introduction function.

    Args:
        request (pytest.FixtureRequest): The pytest fixture request object.
        caplog (pytest.LogCaptureFixture): The pytest log capture fixture.
    """
    # Run the log_introduction function
    name = request.config.getoption("name")
    main.log_introduction(name)

    # Check the logging output
    expected_output = "Hello World!\n" if name is None else f"Hello {name}!\n"
    assert caplog.text.endswith(expected_output)
