# Python Template

A template repository for Python projects.

## Table of Contents

-   [Requirements](#requirements)
-   [Getting Started](#getting-started)
-   [Running the Package](#running-the-package)
-   [Running the Tests](#running-the-tests)
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

## Running the Tests

To ensure your code works as expected, running tests frequently is essential. This project leverages `pytest` as its testing framework. Here's how to execute your tests:

1.  **Install Testing Dependencies**: If you haven't already installed the optional testing dependencies, you can do so by running:

```sh
pip install -e .[test]
```

2.  **Write and Organize Your Tests**: Create Python files with the `test_` prefix (e.g., `test_module.py`) in the `tests` directory. Inside these files, write test functions that also use the `test_` prefix (e.g., `test_my_function()`). This naming convention enables automatic test discovery by pytest.
3.  **Run Your Tests**: To run all tests in the `tests` directory, simply execute:

```sh
pytest
```

If you want to target specific tests, pytest provides various options to refine test collection. Here are some commonly used examples that can be combined:

```sh
pytest tests/test_main.py  # Run all tests in a file
pytest tests/test_main.py::test_log_intro  # Execute a specific test in a file
pytest -k log  # Use keywords to only run tests with log in the name
pytest -m skip  # Find any tests with a skip marker and run them
```

4. **Viewing Logs**: By default, pytest captures all logging output and only displays it for failing tests. Doing so keeps the terminal output clean and allows the user to easily see a summary of what is most important. In the event that you want to modify this behavior, you can use the following commands to view logging statments either during or after test execution:

-   **Live Logging**: The following command enables real-time logging during test execution:

```sh
pytest --log-cli-level DEBUG  # Show DEBUG logs and above during a test
```

-   **Summary Logs**: Use the `-rP` flag to display captured logs in the test summary report.

```sh
pytest -rP  # Show logs at the end of a test session based on the configured logging level
```

5.  **Use Custom Arguments**: All custom arguments available when running the package directly have also been configured to work with pytest. Note that unless you provide arguments to see logs (like those mentioned above), you'll only see logging output for failing tests.

```sh
pytest --log_level DEBUG  # Set the level of logs
pytest --log_format TIME  # Set the format of logs
pytest -v  # Enable verbose logging
```

6.  **Check Test Results**: After running the tests, `pytest` will provide a summary of the test results in the terminal. It will show which tests passed, which failed, and any errors encountered.
7.  **Capture Output**: If you need to capture the output of your functions during testing, you can use the `capsys` fixture provided by `pytest`. This is useful for verifying print statements and other output.
    -   If wanting to verify the output of logging statements, the `caplog` fixture will need to be used instead.
8.  **Generate Test Reports**: For more detailed test reports, you can use additional plugins like `pytest-html` to generate HTML reports:

```sh
pytest --html=htmlcov/report.html --self-contained-html
```

By following these steps, you can ensure your code is throughly tested and maintain high code quality throughout your project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
