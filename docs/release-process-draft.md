## Development & PR Workflow

1. Cut a topic branch from `main`:

    ```bash
    git checkout main
    git pull origin main
    git checkout -b feature/your-feature-name
    ```

2. Implement your changes. Do not modify the version string in `pyproject.toml` and do not edit `CHANGELOG.md` directly.

3. Create change fragments inside the `changes/` directory detailing any modifications that should be included in the changelog. Consult [Changelog Fragments](changelog-fragments.md) for naming and formatting specifications.

4. Verify code quality locally before pushing:

    ```bash
    pre-commit run --all-files
    pytest
    ```

5. Open a Pull Request targeting `main`. GitHub Actions will validate:
    - Code formatting and linting.
    - Test suite execution across target Python runtimes.
    - Presence of a valid changelog fragment in `changes/`.

## Phase 1: Release Preparation

Releases are initiated on demand via GitHub Actions once sufficient changes have accumulated on `main`.

1. Navigate to **Actions** $\rightarrow$ **Prepare Release**.
2. Click **Run workflow** against `main`.
3. Select the version bump strategy (`patch`, `minor`, `major`, or provide an explicit SemVer string `X.Y.Z`).

### Automated Actions in Phase 1

The `prepare-release.yml` workflow executes the following:

1. Creates an isolated branch: `release/vX.Y.Z`.
2. Updates `pyproject.toml` and regenerates the lockfile using the package manager.
3. Runs the changelog compilation script:
    - Aggregates all fragments in `changes/` into a structured release section in `CHANGELOG.md`.
    - Unlinks the processed fragment files while preserving `.gitkeep`.
4. Executes test and lint suites to ensure the updated lockfile and changelog pass all checks.
5. Commits the changes (`chore(release): bump version to vX.Y.Z`) and pushes the release branch.
6. Opens a Release Pull Request targeting `main`.

## Phase 2: Review and Verification (Stop & Wait)

The Release PR acts as an explicit staging gate before packages are built and published.

### Maintainer Checklist

1. Review the generated `CHANGELOG.md` section within the PR diff.
2. Polish release notes if necessary (e.g., clarify breaking change instructions or group related features).
3. If manual edits are made, commit them directly to the `release/vX.Y.Z` branch.
4. Verify that all CI checks on the Release PR are green.
5. Merge the PR into `main` using **Create a Merge Commit** or **Rebase and Merge** (avoid squash merging if preserving the explicit release commit metadata is desired).

To cancel a release, close the PR and delete the `release/vX.Y.Z` branch. No tags or package builds will be triggered.

## Phase 3: Automated Publishing

Merging the Release PR triggers the `publish.yml` workflow on `main` via path matching on `pyproject.toml`.

### Automated Pipeline Steps

1. Extracts the canonical version from `pyproject.toml` at `HEAD`.
2. Verifies that the corresponding Git tag does not already exist.
3. Creates and pushes an annotated Git tag: `vX.Y.Z`.
4. Builds the standard source distribution (`sdist`) and binary wheel (`wheel`).
5. Calculates SHA256 checksums for all distribution artifacts and writes them to `dist/SHA256SUMS`.
6. Extracts the version-specific section from `CHANGELOG.md`.
7. Creates a GitHub Release matching `vX.Y.Z`, attaching the release notes, distribution files, and checksum manifests.
8. Publishes the distribution packages to PyPI via OIDC Trusted Publishing.

## Hotfix Procedure

When an urgent patch must be released:

1. Create a hotfix branch from the latest release tag:

    ```bash
    git checkout -b hotfix/critical-patch v1.2.0
    ```

2. Apply the fix and add a corresponding `changes/` fragment (`<id>.fixed.md` or `<id>.security.md`).
3. Open a PR targeting `main`.
4. Once merged to `main`, run the **Prepare Release** workflow selecting a `patch` bump.
