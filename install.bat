@echo off

REM Execute the configure_template.py script
python configure_template.py
echo.

:start_main_script
REM Prompt user for optional dependencies
set /p dev="Install development dependencies (pre-commit, etc.)? [y/n]: "
set /p lint="Install linting dependencies (ruff, etc.)? [y/n]: "
set /p tests="Install testing dependencies (pytest, etc.)? [y/n]: "

REM Ensure pip is up to date in current environment
python -m pip install -U pip

REM Create a virtual environment
python -m venv .venv

REM Activate the virtual environment
call .venv\Scripts\activate

REM Ensure pip is up to date in the virtual environment
python -m pip install -U pip

REM Build combined dependencies string
set "deps="
if /i "%dev%"=="y" set "deps=%deps%dev,"
if /i "%lint%"=="y" set "deps=%deps%lint,"
if /i "%tests%"=="y" set "deps=%deps%tests,"

REM Remove the trailing comma if there are any dependencies
if not "%deps%"=="" set "deps=%deps:~0,-1%"

REM Install dependencies (if deps is empty, this will just install base package)
if "%deps%"=="" (
    pip install -e .
) else (
    pip install -e .[%deps%]
)

echo Setup complete. Virtual environment created and dependencies installed.
:end_main_script

REM Create a temporary batch file to store the main script
setlocal EnableDelayedExpansion
set "this_file=%~f0"
set "temp_file=%~dp0temp.bat"
set "copy_lines=0"

REM Copy the main script to the temporary batch file
echo @echo off>"%temp_file%"
echo.>>"%temp_file%"
for /f "delims=" %%i in ('findstr /n "^" "%this_file%"') do (
    set "line=%%i"
    set "line=!line:*:=!"
    if "!line!"==":start_main_script" (
        set "copy_lines=1"
    ) else if "!line!"==":end_main_script" (
        set "copy_lines=0"
    ) else if !copy_lines! equ 1 (
        if "!line!"=="" (
            echo.>>"%temp_file%"
        ) else (
            echo !line!>>"%temp_file%"
        )
    )
)

REM Cleanup by deleting the configuration script and replacing this script with the temporary script
del configure_template.py
move /Y "%temp_file%" "%this_file%"
