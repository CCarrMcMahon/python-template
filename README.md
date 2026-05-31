# Python Template

A reusable Python project template.

## Getting Started

### Prerequisites

- **Python**: Version 3.12 or higher.
- **Git**: For version control and cloning the repository.
- **uv**: For virtual environment management and dependency syncing.
    - Install uv globally using pip: `pip install uv`

### Installation

```pwsh
# 1. Clone the repository
git clone git@github.com:CCarrMcMahon/python-template.git
cd python-template

# 2. Install Dependencies (Dev Mode includes linting/testing tools)
uv sync

# 3. Activate Virtual Environment and Install Hooks
.\.venv\Scripts\activate
pre-commit install
cp .\hooks\post-commit .\.git\hooks\post-commit
```

## Usage

This template includes a simple CLI example. It can be run in two different ways:

```pwsh
# 1. As a command
app -h

# 2. As a module
python -m python_template -h
```

## After Using This Template

Update these values first so your new project has the right identity:

1. **Project metadata** in `pyproject.toml`
    - `[project].name`
    - `[project].description`
    - `[project].authors`
    - `[project.urls].Repository`
2. **Package import path**
    - Rename `src/python_template/` to your package name (for example, `src/my_project/`).
    - Update imports and module references from `python_template` to your new package name.
3. **CLI command name**
    - Update `[project.scripts]` (currently `app`) to your preferred command.
    - Update `prog` in `src/python_template/cli.py` to match.
4. **README usage examples**
    - Replace `python_template` references in script/module examples with your new package name.
