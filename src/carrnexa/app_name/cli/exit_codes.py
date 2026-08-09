from __future__ import annotations

from enum import IntEnum


class ExitCode(IntEnum):
    """Enumeration of exit codes for the CLI application."""

    SUCCESS = 0
    EXCEPTION = 1
    USAGE = 2


__all__ = ["ExitCode"]
