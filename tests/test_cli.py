from __future__ import annotations

from typer.testing import CliRunner

from carrnexa.app_name.cli.example import EXAMPLE_ENTRY_MSG, EXAMPLE_SUCCESS_MSG
from carrnexa.app_name.cli.exit_codes import ExitCode
from carrnexa.app_name.cli.main import app

HELP_HEADER = "Usage: root [OPTIONS] COMMAND [ARGS]..."

runner = CliRunner()


def test_app_shows_help_without_args() -> None:
    result = runner.invoke(app)
    assert result.exit_code == ExitCode.USAGE
    assert HELP_HEADER in result.stdout


def test_app_shows_help_with_help_flags() -> None:
    for flag in ["--help", "-h"]:
        result = runner.invoke(app, [flag])
        assert result.exit_code == ExitCode.SUCCESS
        assert HELP_HEADER in result.stdout


def test_example_command_succeeds_with_no_flags() -> None:
    result = runner.invoke(app, ["example"])
    assert result.exit_code == ExitCode.SUCCESS
    assert result.stdout == f"{EXAMPLE_ENTRY_MSG}\n{EXAMPLE_SUCCESS_MSG}\n"


def test_example_command_fails_with_fail_flags() -> None:
    for flag in ["--fail", "-f"]:
        result = runner.invoke(app, ["example", flag])
        assert result.exit_code == ExitCode.EXCEPTION
        assert result.stdout == f"{EXAMPLE_ENTRY_MSG}\n"
