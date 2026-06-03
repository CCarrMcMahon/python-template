# Commit Message Instructions

## Purpose

Commit messages in this repo are meant to provide a condensed summary of the changes being committed. Since all code changes are expected to be reviewed in associated PRs, these messages are often not reviewed in detail. Instead, they are meant to act like a timeline, allowing reviewers to quickly pinpoint moments in time that they may be interested in.

## Format

Every commit message should follow the same format, consisting of a subject line and sometimes a body.

### Subject Line

The subject line is always required and should be a single, well formatted sentence ending in a period. If properly written, readers should be able to understand the fundamental change being made and is often all that is required. If the commit contains multiple unrelated changes, the message should describe the overall theme, falling back to the most important change if a theme cannot be easily identified or described.

### Body

The body is an optional section separated from the subject line by a blank line and is rarely needed. In the rare cases where the subject line cannot fully capture the change, the body can be used to provide additional context. This is often the case when a commit contains multiple related changes that are best described together, or when a change is complex and requires more explanation. Since the code changes are expected to be reviewed in associated PRs, the body should not be used to provide implementation details or code snippets, but rather to provide additional context or motivation for the change.

## General Rules

- Write commits from the perspective of the author, describing why the change was made and what it does, not how it was implemented.
- Use past tense to better reflect the feeling of the author when they made the change.
- Capture why the change is most likely being made, focusing on more detailed motivations rather than high-level themes.
- Use ASCII punctuation only (no smart quotes or em-dashes).
- Prioritize new information over refactors or formatting changes.

## What to Avoid

- Do not use present tense, as it can make the commit message feel like a to-do item rather than a completed change.
- Do not use conventional commit prefixes (no "feat:", "fix:", etc.).
- Do not overuse words like clarity, consistency, or readability.
- Do not list files changed or exhaustive bullet points.
- Do not include implementation details or code snippets in the commit message.
- Do not use emojis or non-standard characters.
