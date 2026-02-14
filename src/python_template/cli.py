from __future__ import annotations

import argparse
import logging
from enum import IntEnum

from python_template.logging_utils import initialize_logging

logger = logging.getLogger(__name__)


class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


def _init_cli_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser for the cli.

    Returns:
        parser (argparse.ArgumentParser): Configured argument parser for the cli.
    """
    parser = argparse.ArgumentParser(
        prog="app", description="Command-line interface for this package."
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


def main() -> int:
    """The cli entry point for this package.

    Parses command-line arguments and executes the app.

    Returns:
        exit_code (int): An exit code indicating the result of app execution.
    """
    parser = _init_cli_parser()
    args = parser.parse_args()

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


if __name__ == "__main__":
    raise SystemExit(main())
