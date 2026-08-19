# Release Process

This document describes the release process for this repository.

The process uses a trunk-based Git tag flow. Changes are prepared on `main`, staged through a release branch, and finalized after the approved release is merged back into `main`.

## Architecture

The release flow has three main parts:

- **Development on `main`**: Most work lands on `main` through topic branches and pull requests. Small maintenance edits may be committed more directly when that is reasonable for the repository.
- **Release preparation**: The release-preparation workflow creates a short-lived `release/vX.Y.Z` branch with the version bump, compiled changelog, fragment cleanup, and final validation, then opens it for review before anything is tagged or released.
- **Tag and release**: After the approved release branch is merged back into `main`, automation creates the version tag from the release commit, creates a GitHub Release with release notes and artifacts, and optionally publishes the package to a configured package index.

```mermaid
---
title: Example Release Workflow
config:
    logLevel: 'debug'
    themeVariables:
        'git0': '#c21f1f'
        'git1': '#1f6fc2'
        'git2': '#1fc21f'
        'git3': '#c2c21f'
    gitGraph:
        parallelCommits: true
---
gitGraph:
    commit id: "Current Release" tag: "v1.5.2" type: HIGHLIGHT

    branch "fix/34-auth-fails-on-azure"
    checkout "fix/34-auth-fails-on-azure"
    commit id: "#34: Add failing test"
    commit id: "#34: Fix auth handling"
    checkout main
    merge "fix/34-auth-fails-on-azure" id: "Merge PR #34"

    branch "feature/package-config"
    checkout "feature/package-config"
    commit id: "Add configuration option"
    commit id: "Document behavior"
    checkout main
    merge "feature/package-config" id: "Merge PR #35"

    commit id: "Remove trailing space"
    commit id: "Run Release Workflow" type: REVERSE

    branch "release/v1.6.0"
    checkout "release/v1.6.0"
    commit id: "Bump version"
    commit id: "Assemble changelog"
    checkout main
    merge "release/v1.6.0" id: "New Release" tag: "v1.6.0" type: HIGHLIGHT
```

## Workflow

### Everyday Changes

For most user-facing changes, use a topic branch and a pull request.

1. Start from an up-to-date `main` branch.

    ```bash
    git checkout main
    git pull origin main
    git checkout -b feature/your-change-name
    ```

2. Work iteratively on the branch.
    - Make changes, updating tests, documentation, configuration, or metadata as needed.
    - When the changes should appear in the next release notes, add or update fragments under `changes/<change-id>/`. See [Changelog Fragments](changelog-fragments.md) for naming and writing guidance.
    - Make sure the repository Git hooks are installed so pre-commit runs on each commit, and fix any issues the hooks report.
    - Run pytest during development as needed.

3. Prepare the pull request.
    - Before opening the pull request, run the checks that match the scope of the change. For broad changes, run the full local checks:

        ```bash
        uv run pre-commit run --all-files
        uv run pytest
        ```

    - Open a pull request targeting `main`.
    - If the pull request changes during review, rerun the relevant checks before merging.

4. Merge the pull request once the chosen checks and review expectations have been satisfied.

> **Note**
> Normal work does not usually bump the package version or edit `CHANGELOG.md`. Those updates are normally part of release preparation.

Small maintenance changes can be handled more directly when that fits the repository. For example, fixing a typo in internal documentation may not need the same pull request flow as a user-facing behavior change.

### Release Preparation

Start release preparation when the accumulated changes on `main` are ready for a release. The planned `prepare-release` workflow should automate this sequence; until that workflow exists, use the same sequence manually.

1. Choose the next version using Semantic Versioning:
    - **Patch** for backwards-compatible bug fixes and small documentation-only release updates.
    - **Minor** for backwards-compatible features or meaningful behavior improvements.
    - **Major** for breaking changes that require users or maintainers to adjust how they use the project.

2. Create a release branch from `main`.

    ```bash
    git checkout main
    git pull origin main
    git checkout -b release/vX.Y.Z
    ```

3. Update the package version with `uv version`. Use either an explicit version or a SemVer bump:

    ```bash
    uv version 1.6.0
    uv version --bump minor
    ```

    This updates the package metadata and keeps `uv.lock` in sync.

4. Compile the fragments under `changes/` into a new version section in `CHANGELOG.md`.

5. Remove the processed fragment files and directories from `changes/`.

6. Run the release checks.

    ```bash
    uv run pre-commit run --all-files
    uv run pytest
    ```

7. Commit the release-preparation changes.

    ```bash
    git add pyproject.toml uv.lock CHANGELOG.md changes
    git commit -m "Prepare release vX.Y.Z"
    ```

8. Push the release branch and open a release pull request targeting `main`.

    ```bash
    git push origin release/vX.Y.Z
    ```

When adding release automation, keep the changelog compilation and release validation logic in repository scripts where practical, so the same checks can run locally and in GitHub Actions.
