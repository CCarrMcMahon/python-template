from __future__ import annotations

import argparse
import logging
from collections.abc import Sequence
from enum import IntEnum

from python_template.logging_utils import initialize_logging

logger = logging.getLogger(__name__)


class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


def _init_cli_parser(*, prog: str = "app") -> argparse.ArgumentParser:
    """Create and configure the argument parser for the cli.

    Args:
        prog (str): The name of the program to display in help messages. Defaults to "app".

    Returns:
        parser (argparse.ArgumentParser): Configured argument parser for the cli.
    """
    parser = argparse.ArgumentParser(
        prog=prog, description="Command-line interface for this package."
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="Enable verbose output.",
    )
    parser.add_argument(
        "--fail", action="store_true", default=False, help="Force the main logic to fail."
    )

    return parser


def execute_app(fail: bool = False) -> bool:
    """Execute the app.

    Args:
        fail (bool): If True, simulate a failure.

    Returns:
        success (bool): Whether execution was successful.
    """
    logger.info("Executing the app.")
    logger.debug("This message should only be shown in verbose mode.")

    try:
        if fail:
            logger.warning("A forced failure is about to occur.")
            raise RuntimeError("Forced failure triggered.")
    except Exception as exc:
        logger.error("An exception was raised while executing the app: %s", exc)
        return False

    logger.info("App finished executing.")
    return True


def main(argv: Sequence[str] | None = None, *, prog: str = "app") -> int:
    """The cli entry point for this package.

    Parses command-line arguments and executes the app.

    Args:
        argv (Sequence[str] | None): Optional list of command-line arguments to parse. If None,
            defaults to sys.argv. Defaults to None.
        prog (str): The name of the program to display in help messages. Defaults to "app".

    Returns:
        exit_code (int): An exit code indicating the result of app execution.
    """
    parser = _init_cli_parser(prog=prog)
    args = parser.parse_args(argv)

    verbose: bool = args.verbose
    fail: bool = args.fail

    # Initialize logging based on verbosity
    initialize_logging(verbose)

    logger.info("Beginning execution...")
    success = execute_app(fail)
    if not success:
        logger.error("Execution failed.")
        return ExitCode.FAILURE

    logger.info("Execution succeeded.")
    return ExitCode.SUCCESS
