from __future__ import annotations

from typer import Typer

from carrnexa.app_name.cli import example

app = Typer(
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
    help="CarrNexa CLI starter for this package.",
)
app.add_typer(example.app, name="example")

if __name__ == "__main__":
    app()


__all__ = ["app"]
