# Release Process

This template uses a main-plus-tags release flow with release preparation separated from release publication.

## Principles

- `main` is the integration branch for accepted work, not a promise that every commit is released.
- Normal feature and bugfix pull requests should not bump the package version.
- User-facing changes should leave release-note fragments under `changes/` instead of editing `CHANGELOG.md` directly.
- Release-prep pull requests turn accumulated fragments into versioned release metadata.
- Manually created semantic version tags publish the exact prepared commit.

## Workflow

1. Normal feature and bugfix pull requests add code, tests, docs, and any needed release-note fragments under `changes/`.
2. `main` accumulates accepted changes without requiring a package version bump for every merge.
3. A release-prep pull request bumps the package version, updates `uv.lock`, assembles the accumulated fragments into `CHANGELOG.md`, and deletes the consumed fragments.
4. A manually created semantic version tag, such as `v0.3.0`, publishes the release from the prepared `main` commit.

The intended automation is for pull requests and pushes to `main` to run CI, and for semantic version tags to run the release workflow. `CHANGELOG.md` is the source for the GitHub release notes.

### 1. Normal Pull Requests

For normal work, keep the pull request focused on the behavior being changed.

1. Make the code, test, and documentation changes needed for the work.
2. Add one or more release-note fragments under `changes/` when the change is user-facing.
3. Do not update `pyproject.toml` just to bump the package version.
4. Do not edit `CHANGELOG.md` directly for normal release notes.
5. Open the pull request against `main` and let CI validate the project when the workflow is available.

Add a release-note fragment when the change affects users, CLI behavior, package behavior, public APIs, supported configuration, documented workflows, or shipped dependencies. Test-only changes, refactors, formatting, and internal cleanup usually do not need a fragment.

### 2. Prepare a Release Pull Request

Release preparation happens in a dedicated release-prep pull request. The prep branch should be temporary, such as `release/v1.3.0`, and should be created from the current `main` branch.

1. Create a release-prep branch from `main`, such as `release/v0.3.0`.
2. Bump the version with `uv version 0.3.0`; this updates `pyproject.toml`, re-locks `uv.lock`, and syncs the environment by default.
3. Move the accumulated `changes/` fragments into a new `CHANGELOG.md` section for the release.
4. Delete the consumed `changes/` fragments.
5. Update the changelog comparison links.
6. Run the local checks: `uv sync --frozen`, `uv run ruff check`, `uv run ruff format --check`, `uv run pytest`, and `uv build`.
7. Commit the release metadata changes.
8. Open and merge the release-prep pull request into `main` after CI passes.

For now, prepare the release manually. A future manual GitHub Actions workflow may automate these steps by running from trusted workflow code on `main`, creating the release-prep branch, committing the generated files, and opening the pull request.

### 3. Cut the Release

Create an annotated tag from the merge commit on `main`, then push it.

```bash
git checkout main
git pull
git tag -a v0.3.0 -m "v0.3.0"
git push origin v0.3.0
```

The planned release workflow should rerun linting and tests, build the package, extract the matching version notes from `CHANGELOG.md`, create or update the GitHub release, and upload the contents of `dist/`.

## Release-Note Fragments

Release-note fragments are intentionally small. Use a separate fragment when one pull request contains changes that belong in different changelog categories.

Suggested fragment names:

```text
changes/123.added.md
changes/124.changed.md
changes/125.fixed.md
changes/126.removed.md
```

Use the filename pattern `changes/<id-or-slug>.<category>.md`. Prefer issue or pull request numbers when they are available. Use a short slug when the work has no stable tracking number. Use one of these categories:

- `added`
- `changed`
- `deprecated`
- `removed`
- `fixed`
- `security`

Avoid commit hashes because they are hard to create by hand, change during rebases and amendments, and tie release notes to implementation history instead of the user-facing change.

A future helper script may create fragments and enforce this convention:

```bash
uv run python scripts/add_change.py fixed "Fix config loading when the file is missing"
```

The helper should create `changes/` when needed, validate the category, detect an issue number from the current branch when possible, fall back to a safe slug, avoid overwriting existing fragments, and write a properly formatted bullet.

## Guardrails

### Automation Boundaries

- Version bumps, changelog assembly, and tag creation stay out of normal feature and bugfix pull requests.
- A future prepare-release workflow may automate the release-prep branch and pull request, but it should not create tags or publish releases.
- The planned release workflow should remain tag-driven so publishing requires an explicit human decision about the exact commit to release.

### Validation Responsibilities

Each workflow validates a different stage of the release path.

- CI should validate general project health on pull requests and pushes to `main`. It should run release metadata validation, Ruff linting, Ruff formatting checks, and pytest's default test discovery.
- Release-prep validation checks that the planned version is ready before the release-prep pull request is merged. It should verify that `pyproject.toml`, `uv.lock`, `CHANGELOG.md`, and the target tag version all agree, and that the versioned changelog notes are present.
- The tag-triggered release workflow should validate the exact commit being published. It should rerun the release metadata checks with the pushed tag, rerun linting and tests, build the distributions, extract the matching changelog notes, and publish the GitHub release assets.

The release workflow should intentionally fail when versioned changelog notes are missing. Do not create empty notes during the release job; prepare them before tagging so the published release has meaningful content.
