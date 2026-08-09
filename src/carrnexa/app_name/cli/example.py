from __future__ import annotations

from typing import Annotated

import typer

EXAMPLE_ENTRY_MSG = "Running the example command..."
EXAMPLE_FAIL_MSG = "Example command failed due to fail option."
EXAMPLE_SUCCESS_MSG = "Example command completed successfully."

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
    print(EXAMPLE_ENTRY_MSG)
    if fail:
        raise RuntimeError(EXAMPLE_FAIL_MSG)
    print(EXAMPLE_SUCCESS_MSG)


__all__ = ["EXAMPLE_ENTRY_MSG", "EXAMPLE_FAIL_MSG", "EXAMPLE_SUCCESS_MSG", "app"]
