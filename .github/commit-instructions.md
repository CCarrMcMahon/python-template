# Commit Message Instructions

## Purpose

Commit messages in this repo should capture the main change in meaning, behavior, structure, or framing introduced by the commit. Since detailed review usually happens by reading the diff or the surrounding code review, the commit message should act more like a precise timeline marker than a miniature change log. A reader scanning history should be able to tell what materially changed in the project, not just that something was improved.

## Format

Every commit message should have a subject line and may include a short body when needed.

### Subject Line

The subject line is always required and should be a single sentence ending in a period. It should name the dominant change at the level of concept, behavior, structure, or interface, rather than collapsing the change into a vague editorial benefit.

A good subject line answers this question:

"What is materially different after this commit?"

If the commit contains several related changes, summarize the shared idea that ties them together. If it contains unrelated changes, summarize the highest-leverage change rather than trying to mention everything.

If the subject line mostly says where the edit happened, rewrite it until it says what new claim, distinction, or structure now exists.

### Body

The body is optional and should stay short. Use it when a single sentence would hide an important second dimension of the change, such as scope, motivation, or a closely related supporting shift.

The body should usually be one or two short sentences. It should add context, not inventory every file edit, section rewrite, or implementation step.

## How to Choose the Summary

When deciding what the commit is "about," prefer this order:

1. The new concept, invariant, behavior, or framing established by the change.
2. The main structural or interface change that enables that outcome.
3. The motivation or cleanup angle, but only when the commit is genuinely just cleanup.

In practice:

- Prefer concrete domain nouns from the diff over generic quality words.
- Name the new framing or distinction when a rewrite formalizes existing material.
- For documentation commits, describe what the document now defines, separates, or argues, not that it was made clearer.
- Mention at most one or two concrete anchors; these should usually be concepts, behaviors, or interfaces rather than section titles or file names.
- If the change reclassifies or reframes material, name that shift directly instead of saying the material was revised.
- If a stronger verb is available, prefer it over generic verbs like "updated" or "improved."

Prefer summaries shaped like these:

- "Defined X around Y."
- "Separated X from Y in Z."
- "Reframed X as Y with explicit Z."
- "Established X as the basis for Y."

## General Rules

- Write commits from the perspective of the author, describing what changed and why it matters at a project-history level, not how it was implemented.
- Use past tense to better reflect the feeling of the author when they made the change.
- Prefer the conceptual or behavioral delta over generic motivation language.
- Use ASCII punctuation only (no smart quotes or em-dashes).
- Prioritize semantic, behavioral, or structural changes over refactors or formatting changes.
- If a change mainly formalized, constrained, or reorganized existing material, say what new structure or distinction now exists.

## What to Avoid

- Do not use present tense, as it can make the commit message feel like a to-do item rather than a completed change.
- Do not use conventional commit prefixes (no "feat:", "fix:", etc.).
- Do not let words like clarity, completeness, consistency, readability, cleanup, polish, or preparation become the entire message unless they are truly the main point of the commit.
- Do not default to generic summaries that could describe many unrelated commits.
- Do not use section names, file names, or document regions as the main payload of the message unless renaming or reorganizing those parts is itself the substantive change.
- Do not use the pattern "Revised/Updated X to clarify/improve/explain Y" when a more specific statement about the resulting concept or structure is available.
- Do not list files changed or exhaustive bullet points.
- Do not include implementation details or code snippets in the commit message.
- Do not use emojis or non-standard characters.

## Self-Check

Before finalizing a commit message, check the following:

1. If you remove the file name, section title, or document area from the sentence, does a substantive claim remain?
2. Could the same sentence plausibly describe many unrelated commits in the same repo? If so, rewrite it.
3. Does the sentence name the resulting concept, distinction, behavior, or structure rather than the act of revising it?

## Example

Weak:

"Revised the design notes to clarify the framework and operational context."

Stronger:

"Defined the system boundaries and failure semantics in the design notes."
