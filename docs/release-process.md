# Release Process

This document outlines the branching strategy, changelog aggregation model, and automated release pipeline for this repository.

## Architecture Overview

The architecture used is known as a trunk-based Git Tag Flow paired with an asynchronous Release Pull Request ("Stop & Wait") pattern. The following diagram illustrates the flow of changes from development to release:

```mermaid
gitGraph
    commit id: "Current Release" tag: "v1.5.2"

    branch "fix/34-auth-fails-on-azure"
    checkout "fix/34-auth-fails-on-azure"
    commit id: "#34: Testing Fix"
    commit id: "#34: Testing Fix Again"
    checkout main
    merge "fix/34-auth-fails-on-azure" id: "PR #34 merged"

    branch "feature/cli-logging"
    checkout "feature/cli-logging"
    commit id: "Add dependency"
    commit id: "Configure logging"
    commit id: "Add CLI logging flag"
    checkout main
    merge "feature/cli-logging" id: "PR #35 merged"

    commit id: "..."
    commit id: "Run Release Workflow"

    branch "release/v1.6.0"
    checkout "release/v1.6.0"
    commit id: "Bump version"
    commit id: "Compile changelog"
    commit id: "Clean fragments"
    checkout main
    merge "release/v1.6.0" id: "New Release" tag: "v1.6.0"
```

## Branching Model

In general, the repository maintains three types of branches:

- **Trunk (`main`)**: Maintains production-ready code. All commits should enter `main` through approved Pull Requests. Direct pushes to `main` are generally prohibited by branch protection rules to ensure that all changes have been reviewed and validated by CI.
- **Topic Branches (`feature/*`, `fix/*`, etc.)**: Short-lived branches which are usually cut from `main` and focused on a single task. Once the work has been finished, everything gets merged back into the parent branch.
- **Release Branches (`release/vX.Y.Z`)**: Ephemeral staging branches generated automatically by the release preparation workflow. This is where the version bump, changelog compilation, and final validation occur before merging back into `main` and triggering the publishing workflow.
