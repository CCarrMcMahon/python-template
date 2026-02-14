# Python Template

A template for Python projects.

## Getting Started

We use **[uv](https://github.com/astral-sh/uv)** for environment management and dependency syncing.

### Prerequisites

- **Python**: 3.12 or higher
- **uv**: `pip install uv` (or your preferred method)

### Installation

```pwsh
# 1. Clone the repository
git clone git@github.com:CCarrMcMahon/python-template.git
cd python-template

# 2. Initialize Virtual Environment & Sync Dependencies
uv venv
.\.venv\Scripts\activate

# 3. Install Dependencies (Dev Mode includes linting/testing tools)
uv sync
pre-commit install
```

## Usage

This template includes a simple CLI example. You can run it three ways:

```pwsh
# 1. As a script
python .\src\python_template\cli.py

# 2. As a module
python -m python_template.cli

# 3. As a command
pt
```

### Running with Options

```pwsh
# View help
pt -h

# Enable verbose output
pt -v

# Force the main logic to fail
pt --fail
```
