> TODO: Consider making a folder per branch to avoid collisions on fragment names and reduce clutter.

## Why Use Fragments

- **Zero Merge Conflicts:** Prevents parallel pull requests from conflicting on the same lines of `CHANGELOG.md`.
- **Atomic Tracking:** Keeps change documentation co-located with the specific commits and code changes that introduced them.
- **Deterministic Releases:** Allows the release pipeline to compile, categorize, date-stamp, and clean up change notes automatically.

## File Naming Convention

Every Pull Request that alters code, documentation, or behavior must add a markdown file to the `changes/` directory using the following format:

```text
changes/<issue_or_pr_id>.<category>.md
```

- `<issue_or_pr_id>`: The GitHub Issue or Pull Request number (e.g., `142`). If no issue exists, use a short alphanumeric slug (e.g., `cli-auth`).
- `<category>`: The change type suffix matching the standard Keep a Changelog taxonomy.

### Allowed Categories

| Suffix           | Category Heading | Purpose                                                                           |
| :--------------- | :--------------- | :-------------------------------------------------------------------------------- |
| `.breaking.md`   | Breaking Changes | Incompatible API, CLI flag, or configuration modifications.                       |
| `.added.md`      | Added            | New user-facing features or CLI commands.                                         |
| `.changed.md`    | Changed          | Modifications to existing functionality without breaking backwards compatibility. |
| `.deprecated.md` | Deprecated       | Features or flags that will be removed in future versions.                        |
| `.removed.md`    | Removed          | Features or flags that have been eliminated.                                      |
| `.fixed.md`      | Fixed            | Bug fixes and defect corrections.                                                 |
| `.security.md`   | Security         | Vulnerability remediation and security updates.                                   |

## Writing Fragment Content

- Write concise, complete sentences in the imperative or present tense.
- Do not include the bullet point (`-`) prefix; the compiler adds formatting automatically.
- Do not include the PR or Issue number in the text; the compiler appends references based on the file name.
- Use backticks for CLI commands, flags, arguments, class names, and code identifiers.

### Good Examples

```markdown
<!-- changes/104.added.md -->

Add `--output-format` flag to support JSON and YAML output formats in the root CLI.
```

```markdown
<!-- changes/112.fixed.md -->

Resolve broken symlink resolution when parsing directory paths on Windows.
```

```markdown
<!-- changes/118.breaking.md -->

Remove deprecated `--legacy-auth` flag in favor of environment-based token resolution.
```

```markdown
<!-- changes/125.security.md -->

Upgrade minimum cryptography dependency to remediate CVE-XXXX-XXXX.
```

## Compilation and Lifecycle

1. **Development:** The fragment is committed and pushed with the feature branch.
2. **CI Check:** PR validation verifies that at least one valid fragment exists under `changes/`.
3. **Release Execution:** During the release preparation workflow, the aggregation script:
    - Parses all fragment files in `changes/`.
    - Sorts entries into their respective category headings under the new version header in `CHANGELOG.md`.
    - Unlinks the fragment files from the repository.
    - Commits the updated `CHANGELOG.md` and fragment deletions to the release branch.
