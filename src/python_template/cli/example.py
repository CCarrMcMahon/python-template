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
    help="Run the example application.",
)
logger = logging.getLogger(__name__)


@app.callback(invoke_without_command=True)
def execute_app(
    fail: Annotated[
        bool, typer.Option("--fail", "-f", help="Force the example app to fail.")
    ] = False,
) -> None:
    """Execute the app.

    Args:
        fail (bool): If True, simulate a failure.
    """
    logger.info("Executing the app.")
    logger.debug("This message should only be shown in verbose mode.")

    try:
        if fail:
            logger.warning("A forced failure is about to occur.")
            raise RuntimeError("Forced failure triggered.")
    except Exception as exc:
        logger.error("An exception was raised while executing the app: %s", exc)
        raise typer.Exit(code=ExitCode.FAILURE) from exc

    logger.info("App finished executing.")


__all__ = ["ExitCode", "app"]
