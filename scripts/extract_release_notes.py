from __future__ import annotations

import argparse
from pathlib import Path


def find_version_link(changelog_lines: list[str], version: str) -> str | None:
    reference_prefix = f"[{version}]:"
    for line in changelog_lines:
        if line.startswith(reference_prefix):
            return line.removeprefix(reference_prefix).strip()

    return None


def extract_release_notes(changelog_path: Path, version_or_tag: str) -> str:
    version = version_or_tag.removeprefix("v")
    section_header = f"## [{version}]"
    changelog_lines = changelog_path.read_text(encoding="utf-8").splitlines()

    collecting = False
    release_lines: list[str] = []
    for line in changelog_lines:
        if line.startswith(section_header):
            collecting = True
            continue
        if collecting and line.startswith("## ["):
            break
        if collecting:
            release_lines.append(line)

    release_notes = "\n".join(release_lines).strip()
    if not release_notes:
        msg = f"Could not find a changelog section matching {section_header} in {changelog_path}"
        raise SystemExit(msg)

    version_link = find_version_link(changelog_lines, version)
    if version_link:
        release_notes = f"{release_notes}\n\nFull Changelog: [View details]({version_link})"

    return f"{release_notes}\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract the release notes for a version from a Keep a Changelog file."
    )
    parser.add_argument(
        "--tag",
        required=True,
        help="Release tag or version, such as v0.3.0 or 0.3.0.",
    )
    parser.add_argument(
        "--changelog",
        default="CHANGELOG.md",
        help="Path to the changelog file. Defaults to CHANGELOG.md.",
    )
    parser.add_argument(
        "--output",
        help="Optional output path. Defaults to stdout when omitted.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    release_notes = extract_release_notes(Path(args.changelog), args.tag)

    if args.output:
        Path(args.output).write_text(release_notes, encoding="utf-8")
    else:
        print(release_notes, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
