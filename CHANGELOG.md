# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-08-08

### Added

- Added a Keep a Changelog file for template release notes.
- Added shared repository configuration for EditorConfig, Markdownlint, and Prettier.
- Added VS Code file association support so `LICENSE` files open as plain text.
- Added a split CLI smoke-test suite under `tests/cli` covering root help output and example command success and failure flows.
- Added a shared `ExitCode` enum for success, failure, and usage-oriented CLI outcomes.

### Changed

- Updated the project author email in package metadata.
- Simplified editor-specific workspace settings by moving formatting and linting defaults into repository-level config files.
- The example fail path now exits with an explicit CLI failure code instead of surfacing an unhandled exception.
- Simplified the bundled example command behavior and output for clearer CLI smoke testing.

### Removed

- Removed the bundled logging utilities and the root CLI logging callback.
- Removed the direct `colorama` dependency now that the template no longer ships logging utilities.

## [0.1.0] - 2026-07-26

### Added

- Added XML formatter support and updated the recommended VS Code extensions for XML-oriented work.
- Added the `carrnexa.app_name` namespace package layout and a module entrypoint for `python -m carrnexa.app_name`.

### Changed

- Refocused the template around CarrNexa ownership, naming, and package structure.
- Updated project metadata and build configuration to the org-specific template implementation.
- Refreshed the README and lockfile to match the renamed package and new project layout.

[Unreleased]: https://github.com/carrnexa/template-python-cli/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/carrnexa/template-python-cli/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/carrnexa/template-python-cli/releases/tag/v0.1.0
