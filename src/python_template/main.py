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


def main() -> None:
    # Parse arguments
    parser = create_argparser()
    args = parser.parse_args()

    # Log start
    logger.info("Starting the application.")

    # Greet the user
    if args.name:
        logger.info("Hello, %s!", str(args.name))
    else:
        logger.info("Hello World!")

    # Log completion
    logger.info("Application finished.")


if __name__ == "__main__":
    main()
