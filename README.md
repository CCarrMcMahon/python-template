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
