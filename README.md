# CarrNexa Python CLI Template

A starter repository for CarrNexa Python CLI projects. It uses a namespaced `src` layout and includes the default tooling for this project family: `uv`, Typer, Ruff, pytest, and pre-commit.

Use this repository as the base for a new CLI project, then replace the example package, command, and metadata with the project-specific implementation.

## Prerequisites

- **Python**: [Tested on 3.12.10](https://www.python.org/downloads/)
- **Git**: [Tested on 2.55.0](https://git-scm.com/install/)
- **PowerShell 7**: [Tested on 7.6.4](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell?view=powershell-7.6)
- **uv**: [Tested on 0.11.24](https://docs.astral.sh/uv/getting-started/installation/)

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

```pwsh
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

## Reference

- [Release Process](docs/release-process.md)
- [Changelog Fragments](docs/changelog-fragments.md)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)
