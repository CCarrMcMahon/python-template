@echo off

REM Execute the configure_template.py script
python configure_template.py
echo.

:start_main_script
REM Prompt the user for optional dependencies
set /p dev="Install development dependencies (pre-commit, etc.)? [y/n]: "
set /p lint="Install linting dependencies (ruff, etc.)? [y/n]: "
set /p test="Install testing dependencies (pytest, etc.)? [y/n]: "

REM Combine the dependencies into a single string
set "deps="
if /i "%dev%"=="y" set "deps=%deps%dev,"
if /i "%lint%"=="y" set "deps=%deps%lint,"
if /i "%test%"=="y" set "deps=%deps%test,"

REM Remove the trailing comma if there are any dependencies
if not "%deps%"=="" set "deps=%deps:~0,-1%"

REM Start the setup process
echo Updating pip...
python -m pip install -U pip

echo Creating a virtual environment...
python -m venv .venv

echo Activating the virtual environment...
call .venv\Scripts\activate

echo Updating pip in the virtual environment...
python -m pip install -U pip

echo Installing dependencies...
if "%deps%"=="" (
    pip install -e .
) else (
    pip install -e .[%deps%]
)

REM Install pre-commit hooks if pre-commit is installed
if exist ".venv\Scripts\pre-commit.exe" (
    echo Installing pre-commit hooks...
    pre-commit install
)

echo Copying over custom git hooks...
xcopy hooks\* .git\hooks\ /Y /Q

echo.
echo Installation complete.
:end_main_script

REM Display the final instructions
echo.
echo Don't forget to push the changes to your repository by running the following commands:
echo     git add .
echo     git commit -m "Ran install.bat"
echo     git push
echo Once done, you can activate your virtual environment by running: ".venv\Scripts\activate"

REM Create a temporary batch file to store the main script
setlocal EnableDelayedExpansion
set "this_file=%~f0"
set "temp_file=%~dp0temp.bat"
set "copy_lines=0"

REM Copy the main script to the temporary batch file
echo @echo off>"%temp_file%"
echo setlocal>>"%temp_file%"
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
echo endlocal>>"%temp_file%"

REM Cleanup by deleting the configuration script and replacing this script with the temporary script
del configure_template.py >nul 2>&1
move /Y "%temp_file%" "%this_file%" >nul 2>&1
