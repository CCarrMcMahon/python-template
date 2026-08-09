# Release Process

This template uses a simple main-plus-tags release flow.

## Overview

- Pull requests and pushes to `main` run the CI workflow.
- Pushing a semantic version tag like `v0.3.0` runs the release workflow.
- `CHANGELOG.md` is the source for the GitHub release notes.
- Git tags are the release trigger.

## Prepare a Release

1. Update `CHANGELOG.md` with the release notes.
2. Bump the version in `pyproject.toml`.
3. Run the local checks: `uv sync --frozen`, `uv run ruff check`, `uv run pytest`, and `uv build`.
4. Commit the release metadata changes.
5. Merge the release-ready branch into `main`.

## Cut the Release

Create an annotated tag from the merge commit on `main`, then push it.

```bash
git checkout main
git pull
git tag -a v0.3.0 -m "v0.3.0"
git push origin v0.3.0
```

The release workflow reruns linting and tests, builds the package, extracts the matching version notes from `CHANGELOG.md`, creates or updates the GitHub release, and uploads the contents of `dist/`.

## Notes

- CI runs repo-wide Ruff and pytest's default test discovery.
- Version bumps and changelog edits stay manual.
