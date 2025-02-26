import logging
from argparse import ArgumentParser

from python_template.log_management import log_config
from python_template.log_management.log_constants import LogFormat, LogLevel


def create_argparser() -> ArgumentParser:
    """Create an ArgumentParser object with any options available when running the package directly.

    Returns:
        parser (ArgumentParser): The ArgumentParser object after it has been configured.
    """
    # Main argument parser
    parser = ArgumentParser(description="A template repository for Python projects.")

    # Optional arguments
    parser.add_argument(
        "--log_lvl",
        type=str,
        default=LogLevel.INFO.name.lower(),
        choices=[level.name.lower() for level in LogLevel],
        help="The logging level to use for the root logger.",
    )
    parser.add_argument(
        "--log_fmt",
        type=str,
        default=LogFormat.MSECS.name.lower(),
        choices=[format.name.lower() for format in LogFormat],
        help="The logging format to use for the root logger.",
    )
    parser.add_argument(
        "-v",
        "--log_v",
        action="store_true",
        help="Increase the verbosity of the logging output to include more detailed information.",
    )

    return parser


def log_intro() -> None:
    """Log a simple introduction message to show logging state."""
    logger = logging.getLogger(__name__)
    logger.debug("Debug logging enabled.")
    logger.info("Hello, World!")


def main() -> None:
    """The entry point when running the package directly which will populate and parse any configured arguments."""
    parser = create_argparser()
    args = parser.parse_args()

    log_lvl = LogLevel[args.log_lvl.upper()]
    log_fmt = LogFormat[args.log_fmt.upper()]
    log_v = bool(args.log_v)

    if log_v:
        log_lvl = LogLevel.DEBUG
        log_fmt = LogFormat.LINE

    log_config.initialize_root_logger(log_lvl, log_fmt)
    log_intro()


if __name__ == "__main__":
    main()
