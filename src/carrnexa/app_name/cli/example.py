from __future__ import annotations

import logging
from enum import IntEnum
from typing import Annotated

import typer


class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


app = typer.Typer(
    invoke_without_command=True,
    no_args_is_help=False,
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Run the bundled example command.",
)
logger = logging.getLogger(__name__)


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
    logger.info("Running the example command.")
    logger.debug("Verbose logging is enabled for the example command.")

    try:
        if fail:
            logger.warning("A forced failure is about to be triggered.")
            raise RuntimeError("Forced failure triggered for the example command.")
    except Exception as exc:
        logger.error("The example command failed: %s", exc)
        raise typer.Exit(code=ExitCode.FAILURE) from exc

    logger.info("The example command completed successfully.")


__all__ = ["ExitCode", "app"]
