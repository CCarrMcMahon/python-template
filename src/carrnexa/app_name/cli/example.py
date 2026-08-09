from __future__ import annotations

from typing import Annotated

import typer

from carrnexa.app_name.cli.exit_codes import ExitCode

app = typer.Typer(help="Run the bundled example command.")


@app.callback(invoke_without_command=True)
def run_example(
    fail: Annotated[
        bool, typer.Option("--fail", "-f", help="Force the example command to fail.")
    ] = False,
) -> None:
    """Run the bundled example command.

    Args:
        fail (bool): If True, simulate a failure.
    """
    typer.echo("Running the example command...")
    if fail:
        typer.echo("Example command failed due to fail option.", err=True)
        raise typer.Exit(code=ExitCode.FAILURE)
    typer.echo("Example command completed successfully.")


__all__ = ["app"]
