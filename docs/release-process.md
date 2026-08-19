# Release Process

This document outlines the branching strategy, changelog aggregation model, and automated release pipeline for this repository.

## Architecture Overview

The architecture discussed throughout this document follows a trunk-based Git Tag Flow design paired with an asynchronous Release Pull Request ("Stop & Wait") pattern. An example of what this might look like is shown in the diagram below:

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

    commit id: "Run Release Workflow" type: REVERSE

    branch "release/v1.6.0"
    checkout "release/v1.6.0"
    commit id: "Bump version"
    commit id: "Assemble changelog"
    checkout main
    merge "release/v1.6.0" id: "New Release" tag: "v1.6.0" type: HIGHLIGHT
```

## Branching Model

In general, the repository maintains three types of branches:

- **Trunk (`main`)**: Maintains production-ready code. All commits should enter `main` through approved Pull Requests. Direct pushes to `main` are generally prohibited by branch protection rules to ensure that all changes have been reviewed and validated by CI.
- **Topic Branches (`feature/*`, `fix/*`, etc.)**: Short-lived branches which are usually cut from `main` and focused on a single task. Once the work on this branch has been completed, everything gets merged back into the parent branch.
- **Release Branches (`release/vX.Y.Z`)**: Ephemeral staging branches generated automatically by the release preparation workflow. This is where the version bump, changelog compilation, and final validation occur before merging back into `main` and triggering the publishing workflow.
