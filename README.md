# Python Template

A template repository for Python projects.

## Table of Contents

-   [Requirements](#requirements)
-   [Getting Started](#getting-started)
-   [Running the Package](#running-the-package)
-   [Running Tests](#running-tests)
-   [License](#license)

## Requirements

-   **Python 3.12.2 or higher**

## Getting Started

1.  **Clone the Repository**: `git clone git@github.com:CCarrMcMahon/python-template.git`
2.  **Navigate to the Project Directory**: `cd python-template`
3.  **Run the Install Script**: `install.bat`
4.  **Follow the Prompts**: The installation script will guide you through the project setup and allow you to select which optional dependencies to install.
5.  **Activate the Virtual Environment**: `.venv\Scripts\activate`
6.  **Start Developing**: Begin adding your code inside the `src` directory and your tests inside the `tests` directory.

## Running the Package

Once you have set up your environment, you can run the package using Python's module syntax:

```sh
python -m python_template
```

This command will execute the `__main__.py` file in your package. You can also run the package with arguments to control logging:

```sh
python -m python_template --log_level DEBUG  # Set the level of logs
python -m python_template --log_format TIME  # Set the format of logs
python -m python_template --log_level WARNING --log_format LINE  # Combine logging options
python -m python_template --verbose  # Enables verbose logging
python -m python_template -v  # Shorthand for --verbose
```

To see all available command-line options, use the --help flag:

```sh
python -m python_template --help
```

Available arguments:

-   `--log_level`: Set the level of logs (DEBUG, INFO, WARNING, ERROR, CRITICAL)
-   `--log_format`: Set the format of logs (SIMPLE, TIME, MSECS, NAME, FILENAME, LINE)
-   `-v, --verbose`: Enables verbose logging (equivalent to `--log_level DEBUG --log_format LINE`)

## Running Tests

To ensure your code is working correctly, it's important to run tests regularly. This project uses `pytest` for testing. Follow these steps to run your tests:

1.  **Install Testing Dependencies**: If you haven't already installed the optional testing dependencies, you can do so by running:

```sh
pip install -e[tests]
```

2.  **Write Your Tests**: Place your test files in the `tests` directory. Test files should be named `test_*.py` or `*_test.py` to be automatically discovered by `pytest`.
3.  **Run the Tests**: To run all tests, simply execute:

```sh
pytest
```

This command will discover and run all test files in the `tests` directory. Note that by default though, pytest won't display the output from tests in the terminal unless it fails. This is done to reduce clutter in the terminal and can be turned off by adding the `-s` argument in your pytest command.

4.  **Check Test Results**: After running the tests, `pytest` will provide a summary of the test results in the terminal. It will show which tests passed, which failed, and any errors encountered.
5.  **Capture Output**: If you need to capture the output of your functions during testing, you can use the `capsys` fixture provided by `pytest`. This is useful for verifying print statements and other output.
    -   If wanting to verify the output of logging statements, the `caplog` fixture will need to be used instead.
6.  **Run Specific Tests**: To run a specific test file or test function, you can specify its path. For example:

```sh
pytest tests/test_main.py
```

Or to run a specific test function within a file:

```sh
pytest tests/test_main.py::test_log_intro
```

7.  **Control Test Output and Logging**: When running tests, you can control both the test output and logging levels. By default, pytest captures all output unless tests fail. To see output in real-time, use the `-s` flag. You can also control logging using the same arguments as the main package:

```sh
pytest -s  # Show all output in real-time
pytest --log_lvl debug  # Set logging level
pytest --log_fmt simple  # Set logging format
pytest --log_lvl debug --log_fmt line  # Combine logging options
pytest --log_v  # Enable verbose logging
pytest -s --log_v  # Show output and detailed logging
```

Note that pytest's `-v` flag is reserved for pytest's own verbosity and cannot be used for logging control.

8.  **Generate Test Reports**: For more detailed test reports, you can use additional plugins like `pytest-html` to generate HTML reports:

```sh
pytest --html=htmlcov/report.html --self-contained-html
```

By following these steps, you can ensure your code is throughly tested and maintain high code quality throughout your project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
