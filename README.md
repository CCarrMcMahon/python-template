# Python Template

Welcome to the Python Template repository! This template is designed to help you kickstart your Python projects with a clean and efficient structure.

## Features

-   **Layout Design**: The project follows the `src` layout, which organizes your code in a way that prevents common pitfalls. By placing your importable code inside the `src` directory, it ensures that all commands are executed against the actual package, not an in-development copy. This reduces the risk of import errors and makes your development process smoother.
-   **Best Practices**: The template incorporates best practices for Python development, including a clear directory structure, sample configuration files, and guidelines for writing clean, maintainable code.
-   **Ready for Testing**: With the `src` layout, your tests are kept separate from your main codebase, making it easier to manage and run tests without interference.
-   **Easy to Extend**: The template is designed to be easily extendable, allowing you to add new features and modules as your project grows.

## Requirements

-   **Python 3.12.2 or higher**

## Getting Started

1.  **Clone the Repository**: `git clone git@github.com:CCarrMcMahon/python-template.git`
2.  **Navigate to the Project Directory**: `cd python-template`
3.  **Run the Install Script**: `install.bat`
4.  **Follow the Prompts**: The script will prompt you to choose which optional dependencies to install.
5.  **Activate the Virtual Environment**: `.venv\Scripts\activate`
6.  **Start Developing**: Begin adding your code inside the `src` directory and your tests inside the `tests` directory.

## Running Tests

To ensure your code is working correctly, it's important to run tests regularly. This template uses `pytest` for testing. Follow these steps to run your tests:

1.  **Install Testing Dependencies**: If you haven't already installed the optional testing dependencies, you can do so by running:

```sh
pip install -e[tests]
```

2.  **Write Your Tests**: Place your test files in the `tests` directory. Test files should be named `test_*.py` or `*_test.py` to be automatically discovered by `pytest`.
3.  **Run the Tests**: To run all tests, simply execute:

```sh
pytest
```

This command will discover and run all test files in the `tests` directory.

-   Note that by default, pytest won't display the output from tests in the terminal unless it fails. This is done to reduce clutter in the terminal and can be turned off by specifying the `-s` argument in your pytest command.

4.  **Check Test Results**: After running the tests, `pytest` will provide a summary of the test results in the terminal. It will show which tests passed, which failed, and any errors encountered.
5.  **Capture Output**: If you need to capture the output of your functions during testing, you can use the `capsys` fixture provided by `pytest`. This is useful for verifying print statements and other output.
    -   If wanting to verify the output of logging statements, the `caplog` fixture will need to be used instead.
6.  **Run Specific Tests**: To run a specific test file or test function, you can specify its path. For example:

```sh
pytest tests/test_main.py
```

Or to run a specific test function within a file:

```sh
pytest tests/test_main.py::test_log_introduction
```

7.  **Generate Test Reports**: For more detailed test reports, you can use additional plugins like `pytest-html` to generate HTML reports by running your tests with:

```sh
pytest --html="htmlcov/report.html"
```

By following these steps, you can ensure your code is throughly tested and maintain high code quality throughout your project.
