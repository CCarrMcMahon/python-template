import logging
from argparse import ArgumentParser

from python_template.log_management import log_config
from python_template.log_management.log_constants import LogVerbosity


def create_argparser() -> ArgumentParser:
    """Create an ArgumentParser object with any options available when running the package directly.

    Returns:
        parser (ArgumentParser): The ArgumentParser object after it has been configured.
    """
    # Main argument parser
    parser = ArgumentParser(description="A template repository for Python projects.")

    # Optional arguments
    parser.add_argument(
        "--verbosity",
        type=str,
        choices=[verbosity.name.lower() for verbosity in LogVerbosity],
        default=LogVerbosity.NORMAL.name.lower(),
        help="The level of verbosity for the terminal log messages.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose terminal logging (equivalent to `--verbosity verbose`).",
    )

    return parser


def main() -> None:
    """The entry point when running the package directly which will populate and parse any configured arguments."""
    parser = create_argparser()
    args = parser.parse_args()

    verbosity_str: str = args.verbosity
    verbose: bool = args.verbose

    # Set the verbosity level for the logger
    verbosity = LogVerbosity[verbosity_str.upper()]
    if verbose:
        verbosity = LogVerbosity.VERBOSE

    # Set up the root logger with the provided verbosity
    log_config.setup_root_logger(verbosity=verbosity)

    # Log a message to confirm the logger was initialized
    logger = logging.getLogger(__name__)
    logger.debug("Logger initialized with verbosity level: %s", verbosity.name)
    logger.info("Hello, world!")


if __name__ == "__main__":
    main()
