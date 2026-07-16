# Python Template

A reusable Python project template.

## Development

### Prerequisites

- **Python**: Version 3.12 or higher.
- **Git**: For version control and cloning the repository.
- **uv**: For virtual environment management and dependency syncing.
    - Install uv globally using pip: `pip install uv`

### Getting the Code

If you don't already have a local copy of the code, clone the repository and move into the working directory:

```pwsh
git clone git@github.com:CCarrMcMahon/python-template.git
cd .\python-template\
```

### Setup

From the repository root, sync the environment, and activate the virtual environment:

```pwsh
uv sync
.\.venv\Scripts\activate
```

If you are contributing to the repository, also install the pre-commit hooks for formatting and lint checks:

```pwsh
pre-commit install
cp .\hooks\post-commit .\.git\hooks\post-commit
```

## Usage

This template includes a Typer-based CLI with a root command and an example subcommand. The root command is kept as a multi-command app so additional commands can be registered alongside the example command.

```pwsh
# Show root CLI help
app

# Run the example command
app example

# Enable verbose logging
app --verbose example
app -v example

# Force the example command to fail
app example --fail
app example -f
```

The same CLI can also be run as a module:

```pwsh
python -m python_template
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
4. **README usage examples**
    - Replace `python_template` references in script/module examples with your new package name.
