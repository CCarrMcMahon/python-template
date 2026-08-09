# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-08-08

### Added

- Added a Keep a Changelog file for template release notes.
- Added a split CLI smoke-test suite under `tests/cli` covering root help output and example command success and failure flows.
- Added a shared `ExitCode` enum for success, failure, and usage-oriented CLI outcomes.

### Changed

- Removed the bundled logging utilities to keep the template focused on CLI scaffolding.
- Removed the root CLI logging callback and the bundled example command's logging-based behavior.
- The example fail path now exits with an explicit CLI failure code instead of surfacing an unhandled exception.
- Simplified the example command output and test structure so the template demonstrates command-level test organization without exporting test-only string constants.

### Removed

- Removed the direct `colorama` dependency now that the template no longer ships logging utilities.

## [0.1.0] - 2026-08-08

### Added

- Initial template release.

[Unreleased]: https://github.com/carrnexa/template-python-cli/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/carrnexa/template-python-cli/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/carrnexa/template-python-cli/releases/tag/v0.1.0
