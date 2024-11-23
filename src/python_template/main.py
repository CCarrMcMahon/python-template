import logging
from argparse import ArgumentParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_argparser() -> ArgumentParser:
    """Create an ArgumentParser object with any options available when running the package directly.

    Returns:
        parser (ArgumentParser): The ArgumentParser object after it has been configured.
    """
    parser = ArgumentParser(
        description="An example argparse object to handle various arguments for the python_template package."
    )
    parser.add_argument(
        "--name",
        type=str,
        help="An example string argument for your name.",
    )
    return parser


def log_introduction(name: str) -> None:
    """An example function that logs an introduction message.

    Args:
        name (str): The name used in the introduction message.
    """
    if not name or name.strip() == "":
        logger.info("Hello World!")
    else:
        logger.info("Hello %s!", name)


def main() -> None:
    """The entry point when running the package directly which Will populate and parse any configured arguments."""
    parser = create_argparser()
    args = parser.parse_args()
    log_introduction(args.name)


if __name__ == "__main__":
    main()
