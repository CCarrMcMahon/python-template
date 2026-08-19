# Release Process

This document describes the release process for this repository.

The process uses a trunk-based Git tag flow. Changes are prepared on `main`, staged through a release branch, and finalized after the approved release is merged back into `main`.

## Architecture

The release flow has three main parts:

- **Development on `main`**: Most work lands on `main` through topic branches and pull requests. Small maintenance edits may be committed more directly when that is reasonable for the repository.
- **Release preparation**: The release-preparation workflow creates a short-lived `release/vX.Y.Z` branch with the version bump, compiled changelog, fragment cleanup, and final validation, then opens it for review before anything is tagged or published.
- **Tag, release, and publish**: After the approved release branch is merged back into `main`, automation creates the version tag from the release commit, creates a GitHub Release with release notes and artifacts, and optionally publishes the package to a configured package index.

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
