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
cp .\hooks\post-commit .\.git\hooks\post-commit
```

## Usage

This template includes a simple CLI example. It can be run in three different ways:

```pwsh
# 1. As a script
python .\src\python_template\cli.py -h

# 2. As a module
python -m python_template.cli -h

# 3. As a command
pt -h
```
