from __future__ import annotations

from typer.testing import CliRunner

from carrnexa.app_name.cli.exit_codes import ExitCode
from carrnexa.app_name.cli.main import app

ENTRY_MESSAGE_FRAGMENT = "Running the example command"


def test_example_command_succeeds_with_no_flags(runner: CliRunner) -> None:
    result = runner.invoke(app, ["example"])

    assert result.exit_code == ExitCode.SUCCESS
    assert ENTRY_MESSAGE_FRAGMENT in result.stdout
    assert "completed successfully" in result.stdout


def test_example_command_fails_with_fail_flags(runner: CliRunner) -> None:
    for flag in ["--fail", "-f"]:
        result = runner.invoke(app, ["example", flag])

        assert result.exit_code == ExitCode.FAILURE
        assert ENTRY_MESSAGE_FRAGMENT in result.stdout
        assert "failed" in result.output
