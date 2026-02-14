from __future__ import annotations

import argparse
import logging
from enum import IntEnum

from python_template.logging_utils import initialize_logging

logger = logging.getLogger(__name__)


class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


def _build_parser() -> argparse.ArgumentParser:
    """Build and configure the top-level CLI argument parser.

    Returns:
        parser (argparse.ArgumentParser): Configured argument parser for the CLI.
    """
    parser = argparse.ArgumentParser(prog="pt", description="A template for Python projects.")

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


def main_logic(fail: bool = False) -> bool:
    """Main logic of the application.

    Args:
        fail (bool): If True, the function will simulate a failure.

    Returns:
        success (bool): Whether the execution was successful.
    """
    logger.info("Starting to run the main logic.")
    logger.debug("This message should only be shown in verbose mode.")

    try:
        if fail:
            logger.warning("A forced failure is about to occur.")
            raise RuntimeError("Forced failure triggered.")
    except Exception as exc:
        logger.error("An exception was raised in the main logic: %s", exc)
        return False

    logger.info("Main logic completed successfully.")
    return True


def main() -> int:
    """The CLI entry point for the Python template.

    Parses command-line arguments and executes the main logic.

    Returns:
        exit_code (int): Exit code indicating the result of the execution.
    """
    parser = _build_parser()
    args = parser.parse_args()

    verbose: bool = args.verbose
    fail: bool = args.fail

    # Initialize logging based on verbosity
    initialize_logging(verbose)

    logger.info("Beginning execution...")
    success = main_logic(fail)
    if not success:
        logger.error("Execution failed.")
        return ExitCode.FAILURE

    logger.info("Execution completed successfully.")
    return ExitCode.SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())
