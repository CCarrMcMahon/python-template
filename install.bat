@echo off
REM Ensure pip is up to date
python -m pip install -U pip

REM Create a virtual environment
python -m venv .venv

REM Activate the virtual environment
call .venv\Scripts\activate

REM Install main dependencies
pip install -e .

REM Prompt user for optional dependencies
set /p dev="Install development dependencies (pre-commit, etc.)? (y/n): "
if /i "%dev%"=="y" (
    pip install -e .[dev]
)

set /p lint="Install linting dependencies (ruff, etc.)? (y/n): "
if /i "%lint%"=="y" (
    pip install -e .[lint]
)

set /p tests="Install testing dependencies (pytest, etc.)? (y/n): "
if /i "%tests%"=="y" (
    pip install -e .[tests]
)

echo Setup complete. Virtual environment created and dependencies installed.
