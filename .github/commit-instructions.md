# Commit Message Instructions

## Purpose

Commit messages in this repo are meant to provide a condensed summary of the changes being committed. Since all code changes are expected to be reviewed in associated PRs, these messages are often not reviewed in detail. Instead, they are meant to act like a timeline, allowing reviewers to quickly pinpoint moments in time that they may be interested in.

## Format

Every commit message should follow the same format, consisting of a subject line and an optional body:

- **Subject Line**: A single sentence ending in a period summarizing the change.
- **Body**: An optional section that provides additional context, reasoning, or explanations for the change.

## Guidelines

- Separate the subject line from the body with a blank line.
- Only add a body if it provides meaningful context that cannot be captured in the subject line alone.
- Use the body to explain the "why" and "what" of the change, not the "how".
- Prefer plain English over implementation details.
- Use ASCII punctuation only (no smart quotes or em-dashes).
- Prioritize new information over refactors or formatting changes.

## What to Avoid

- Do not use conventional commit prefixes (no "feat:", "fix:", etc.).
- Do not list files changed or exhaustive bullet points.
- Do not include implementation details or code snippets in the commit message.
- Do not use emojis or non-standard characters.
