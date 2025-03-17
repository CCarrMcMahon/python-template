import re
import shutil
from pathlib import Path

DEFAULT_AUTHOR_NAME = "Your Name"
DEFAULT_AUTHOR_EMAIL = "your.email@example.com"
DEFAULT_REPO_URL = "git@github.com:username/my-package.git"
DEFAULT_PROJECT_DESCRIPTION = "An awesome Python project."


def prompt_with_default(value_name: str, default: str) -> str:
    """Prompt the user for a value with a default option.

    Args:
        value_name (str): The name of the value being prompted.
        default (str): The default value to use if the user does not provide a value.

    Returns:
        response (str): The user's response or the default value.
    """
    response = input(f'{value_name} (Default: "{default}"): ').strip()
    if not response:
        return default
    return response


def get_current_package_dir() -> Path | None:
    """Find the current package directory containing __main__.py.

    Returns:
        current_package_dir (Path | None): The current package directory or None if not found.
    """
    # Get all valid top-level directories in the src directory
    package_dirs = [p for p in Path("src").glob("*/")]
    package_dirs = [p for p in package_dirs if not (p.name.startswith(".") or p.name.startswith("_"))]

    # Find a directory containing __main__.py
    current_package_dir = None
    for dir in package_dirs:
        if (dir / "__main__.py").is_file():
            current_package_dir = dir
            break

    return current_package_dir


def get_python_file_paths(directories: list[Path | str]) -> list[Path]:
    """Get all Python file paths in the provided directories.

    Args:
        directories (list[Path | str]): The directories to search for Python files.

    Returns:
        python_file_paths (list[Path]): A list of all Python file paths in the directories
    """
    python_file_paths = []
    for directory in directories:
        dir_path = Path(directory)
        if dir_path.is_dir():
            python_file_paths.extend(dir_path.glob("**/*.py"))

    return python_file_paths


def rename_package(old_package_dir: Path, new_package_name: str) -> bool:
    """Rename the package directory to the new package name.

    Args:
        old_package_dir (Path): The current package directory.
        new_package_name (str): The new package name.

    Returns:
        success (bool): True if the package directory was successfully renamed, False otherwise.
    """
    # Don't do anything if the package directory is already named correctly
    if old_package_dir.name == new_package_name:
        return True

    # Remove the new directory if it exists to avoid conflicts
    new_package_dir = Path("src") / new_package_name
    if new_package_dir.is_dir():
        shutil.rmtree(new_package_dir)

    # Rename the package directory
    old_package_dir.rename(new_package_dir)

    print(f"Renamed package directory: {old_package_dir.name} → {new_package_dir.name}")
    return True


def update_python_files(old_package_name: str, new_package_name: str) -> bool:
    """Update all import statements in Python files in the src and tests directories to use the new package name.

    Args:
        old_package_name (str): The old package name.
        new_package_name (str): The new package name.

    Returns:
        success (bool): True if the imports were successfully updated, False otherwise.
    """
    # Define regex patterns for updating imports
    patterns_and_replacements = {
        re.compile(rf"(\b)import\s+{re.escape(old_package_name)}(\b)"): rf"\1import {new_package_name}\2",
        re.compile(rf"(\b)from\s+{re.escape(old_package_name)}(\b)"): rf"\1from {new_package_name}\2",
        re.compile(rf"(\b){re.escape(old_package_name)}\."): rf"\1{new_package_name}.",
    }

    # Loop through all Python file paths in the src and tests directories
    python_file_paths = get_python_file_paths(["src", "tests"])
    for python_file_path in python_file_paths:
        try:
            python_file_content = ""
            with open(python_file_path) as python_file:
                python_file_content = python_file.read()

            # Apply all replacements
            for pattern, replacement in patterns_and_replacements.items():
                python_file_content = pattern.sub(replacement, python_file_content)

            with open(python_file_path, "w") as python_file:
                python_file.write(python_file_content)
        except Exception as e:
            print(f"Error updating {python_file_path}: {e}")
            return False

    print(f"Updated imports in Python files: {old_package_name} → {new_package_name}")
    return True


def update_pyproject_toml(package_name: str, project_description: str, author_name: str, author_email: str) -> bool:
    """Update the package name, description, and author in pyproject.toml.

    Args:
        package_name (str): The new package name.
        project_description (str): The new project description.
        author_name (str): The new author name.
        author_email (str): The new author email.

    Returns:
        success (bool): True if the values were successfully updated, False otherwise.
    """
    try:
        pyproject_file_content = ""
        with open("pyproject.toml") as pyproject_file:
            pyproject_file_content = pyproject_file.read()

        patterns_and_replacements = {
            re.compile(r'name = "(.*)"'): f'name = "{package_name}"',
            re.compile(r'description = "(.*)"'): f'description = "{project_description}"',
            re.compile(
                r'authors = \[{name = "(.*)", email = "(.*)"}\]'
            ): f'authors = [{{name = "{author_name}", email = "{author_email}"}}]',
            re.compile(r'version = "(.*)"'): 'version = "0.0.0"',
        }

        # Apply all replacements
        for pattern, replacement in patterns_and_replacements.items():
            match = re.search(pattern, pyproject_file_content)
            if not match:
                print(f"Failed to match pattern: {pattern}")
                return False
            pyproject_file_content = pattern.sub(replacement, pyproject_file_content, count=1)

        # Write the updated content back to the file
        with open("pyproject.toml", "w") as pyproject_file:
            pyproject_file.write(pyproject_file_content)

        return True
    except Exception as e:
        print(f"Error updating pyproject.toml: {e}")
        return False


def update_readme_md(
    project_title: str, project_description: str, repo_url: str, repo_name: str, package_name: str, author_name: str
) -> bool:
    """Update the project title, description, repository URL, and cd command in README.md.

    Args:
        project_title (str): The new project title.
        project_description (str): The new project description.
        repo_url (str): The new repository URL.
        repo_name (str): The new repository name.
        package_name (str): The new package name.
        author_name (str): The author's name.

    Returns:
        success (bool): True if the values were successfully updated, False otherwise.
    """
    file_content = ""
    with open("README.md") as file:
        file_content = file.read()

    title_match = re.search(r"# (.*)", file_content)
    description_match = re.search(r"#.*\n\n(.*)", file_content)
    repo_match = re.search(r"`git clone (.*)`", file_content)
    cd_match = re.search(r"`cd (.*)`", file_content)
    package_match = re.search(r"python -m (.*)", file_content)
    author_match = re.search(r'python -m (.*) --name "(.*)"', file_content)
    help_match = re.search(r"python -m (.*) --help", file_content)

    if not all([title_match, description_match, repo_match, cd_match, package_match, author_match]):
        print("Failed to match values in README.md.")
        return False

    file_content = file_content.replace(title_match.group(1), project_title, 1)
    file_content = file_content.replace(description_match.group(1), project_description, 1)
    file_content = file_content.replace(repo_match.group(1), repo_url, 1)
    file_content = file_content.replace(cd_match.group(1), repo_name, 1)
    file_content = file_content.replace(package_match.group(1), package_name, 1)
    file_content = file_content.replace(author_match.group(1), package_name, 1)
    file_content = file_content.replace(author_match.group(2), author_name, 1)
    file_content = file_content.replace(help_match.group(1), package_name, 1)

    with open("README.md", "w") as file:
        file.write(file_content)

    return True


def main() -> None:
    """Main function to configure the project template."""
    print("===== Project Configuration =====")

    author_name = prompt_with_default("Author Name", DEFAULT_AUTHOR_NAME)
    author_email = prompt_with_default("Author Email", DEFAULT_AUTHOR_EMAIL)

    repo_url = prompt_with_default("Repository URL", DEFAULT_REPO_URL)
    repo_name = repo_url.split("/")[-1].replace(".git", "")

    new_package_name = repo_name.replace("-", "_")
    new_package_name = prompt_with_default("Package Name", new_package_name)
    project_title = new_package_name.replace("_", " ").title()
    project_title = prompt_with_default("Project Title", project_title)
    project_description = prompt_with_default("Project Description", DEFAULT_PROJECT_DESCRIPTION)

    current_package_dir = get_current_package_dir()
    if current_package_dir is None:
        print("Failed to find the package directory.")
        return

    # Save the old package name for updating Python files
    old_package_name = current_package_dir.name

    if not rename_package(current_package_dir, new_package_name):
        print("Failed to rename the package directory.")
        return

    if not update_python_files(old_package_name, new_package_name):
        print("Failed to update the Python files.")

    if not update_pyproject_toml(new_package_name, project_description, author_name, author_email):
        print("Failed to update pyproject.toml.")
        return

    if not update_readme_md(project_title, project_description, repo_url, repo_name, new_package_name, author_name):
        print("Failed to update README.md.")
        return

    print("===== Configuration Complete =====")


if __name__ == "__main__":
    main()
