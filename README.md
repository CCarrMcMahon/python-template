# CarrNexa Python CLI Template

CarrNexa's starting point for Python CLI projects. It keeps the setup lean, uses a namespaced `src` layout, and ships with the tooling we want by default: `uv`, Typer, Ruff, pytest, and pre-commit.

The goal is simple: start from something clean, consistent, and easy to grow instead of rebuilding the same scaffolding for every new project.

## What This Template Includes

- A `carrnexa.*` namespace package layout
- A Typer CLI entrypoint with subcommand organization
- `uv` for environment management and dependency syncing
- Ruff, pytest, and pre-commit for day-to-day quality checks
- A small example command you can keep, replace, or delete once your real CLI takes shape
- A `CHANGELOG.md` using the Keep a Changelog format

## Prerequisites

- **Python**: Version 3.12.10 or higher
- **Git**: For cloning and version control
- **Windows shell**: PowerShell 7 for the Windows commands in this README
- **uv**: For virtual environments and dependency management
    - **Unix**: `curl -sSf https://astral.sh/uv/install.sh | sh`
    - **Windows PowerShell 7**: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

## Quickstart

Clone the repository:

```bash
git clone git@github.com:carrnexa/template-python-cli.git
cd template-python-cli
```

Sync dependencies:

```bash
uv sync
```

From there, use `uv run` for the default workflow. It keeps the commands the same on Windows, Linux, and macOS, and avoids shell-specific activation steps in the common path.

```bash
uv run app --help
uv run app example
```

Direct module execution also works:

```bash
uv run python -m carrnexa.app_name --help
```

## Optional: Activate the Virtual Environment

If you prefer to work inside the virtual environment instead of prefixing commands with `uv run`, use the command that matches your shell.

Unix shells:

```bash
source .venv/bin/activate
```

Windows PowerShell 7:

```powershell
.\.venv\Scripts\Activate.ps1
```

Once the environment is active, the commands become:

```bash
app --help
app example
```

## Git Hooks

Install `pre-commit`, then copy the tracked post-commit hook into `.git/hooks`:

```bash
pre-commit install
cp hooks/post-commit .git/hooks/post-commit
```

## Starting a New Project

This template is intentionally close to a real CarrNexa project, so creating a new service or library is mostly a focused rename pass rather than generating a project from scratch.

At minimum, update these places:

- `project.name` in `pyproject.toml`
- `description` and repository URLs in `pyproject.toml`
- `tool.uv.build-backend.module-name`
- `project.scripts`
- `src/carrnexa/app_name`
- Imports that still reference `carrnexa.app_name`

The bundled `example` command is only there to verify the CLI wiring before you replace it with project-specific commands.
