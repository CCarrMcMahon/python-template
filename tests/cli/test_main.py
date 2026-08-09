from __future__ import annotations

from typer.testing import CliRunner

from carrnexa.app_name.cli.exit_codes import ExitCode
from carrnexa.app_name.cli.main import app

HELP_OUTPUT_FRAGMENTS = (
    "Usage:",
    "CarrNexa CLI starter for this package.",
    "example",
)


def test_main_shows_help_without_args(runner: CliRunner) -> None:
    result = runner.invoke(app)

    assert result.exit_code == ExitCode.USAGE
    assert all(fragment in result.stdout for fragment in HELP_OUTPUT_FRAGMENTS)


def test_main_shows_help_with_help_flags(runner: CliRunner) -> None:
    for flag in ["--help", "-h"]:
        result = runner.invoke(app, [flag])

        assert result.exit_code == ExitCode.SUCCESS
        assert all(fragment in result.stdout for fragment in HELP_OUTPUT_FRAGMENTS)
