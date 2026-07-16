from __future__ import annotations

from typing import Annotated

import typer

from python_template.cli import example
from python_template.utils import logging_utils

app = typer.Typer(
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Command-line interface for this package.",
)


@app.callback()
def configure_logging(
    verbose: Annotated[
        bool, typer.Option("--verbose", "-v", help="Enable verbose logging.")
    ] = False,
) -> None:
    logging_utils.initialize_logging(verbose)


app.add_typer(example.app, name="example")

if __name__ == "__main__":
    app()


__all__ = ["app"]
