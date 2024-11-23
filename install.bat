@echo off
REM Prompt user for optional dependencies
set /p dev="Install development dependencies (pre-commit, etc.)? (y/n): "
set /p lint="Install linting dependencies (ruff, etc.)? (y/n): "
set /p tests="Install testing dependencies (pytest, etc.)? (y/n): "

REM Ensure pip is up to date in current environment
python -m pip install -U pip

REM Create a virtual environment
python -m venv .venv

REM Activate the virtual environment
call .venv\Scripts\activate

REM Ensure pip is up to date in the virtual environment
python -m pip install -U pip

REM Install main dependencies
pip install -e .

REM Install selected optional dependencies
if /i "%dev%"=="y" pip install -e .[dev]
if /i "%lint%"=="y" pip install -e .[lint]
if /i "%tests%"=="y" pip install -e .[tests]

echo Setup complete. Virtual environment created and dependencies installed.
