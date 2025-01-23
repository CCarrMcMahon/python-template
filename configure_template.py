import re
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
        str: The value provided by the user or the default value.
    """
    response = input(f'{value_name} (Default: "{default}"): ').strip()
    if not response:
        return default
    return response


def update_pyproject_toml(package_name: str, project_description: str, author_name: str, author_email: str) -> bool:
    """Update the package name, description, and author in pyproject.toml.

    Args:
        package_name (str): The new package name.
        project_description (str): The new project description.
        author_name (str): The new author name.
        author_email (str): The new author email.

    Returns:
        bool: True if the values were successfully updated, False otherwise.
    """
    file_content = ""
    with open("pyproject.toml") as file:
        file_content = file.read()

    name_match = re.search(r'name = "(.*)"', file_content)
    description_match = re.search(r'description = "(.*)"', file_content)
    authors_match = re.search(r'authors = \[{name = "(.*)", email = "(.*)"}\]', file_content)
    if not name_match or not description_match or not authors_match:
        print("Failed to match values in pyproject.toml.")
        return False

    file_content = file_content.replace(name_match.group(1), package_name, 1)
    file_content = file_content.replace(description_match.group(1), project_description, 1)
    file_content = file_content.replace(authors_match.group(1), author_name, 1)
    file_content = file_content.replace(authors_match.group(2), author_email, 1)
    with open("pyproject.toml", "w") as file:
        file.write(file_content)

    return True


def update_main_py(package_name: str) -> bool:
    """Update the package name in __main__.py.

    Args:
        package_name (str): The new package name.

    Returns:
        bool: True if the value was successfully updated, False otherwise.
    """
    file_content = ""
    with open(f"src/{package_name}/__main__.py") as file:
        file_content = file.read()

    match = re.search(r"from (.*) import main", file_content)
    if not match:
        print("Failed to match value in __main__.py.")
        return False

    file_content = file_content.replace(match.group(1), package_name, 1)
    with open(f"src/{package_name}/__main__.py", "w") as file:
        file.write(file_content)

    return True


def rename_package(package_name: str) -> bool:
    """Rename the package directory to the new package name.

    Args:
        package_name (str): The new package name.

    Returns:
        bool: True if the package directory was successfully renamed, False otherwise.
    """
    # Get the package directories in the src directory
    package_dirs = [p for p in Path("src").glob("*/")]
    package_dirs = [p for p in package_dirs if not (p.name.startswith(".") or p.name.startswith("_"))]

    # Get the first package directory found
    current_package_dir = next(iter(package_dirs), None)
    if current_package_dir is None:
        print("No valid package directory found.")
        return False

    # Rename the package directory
    current_package_dir.rename(Path("src") / package_name)

    # Update the package directory name in __main__.py
    return update_main_py(package_name)


def update_test_main_py(package_name: str) -> bool:
    """Update the package name in test_main.py.

    Args:
        package_name (str): The new package name.

    Returns:
        bool: True if the value was successfully updated, False otherwise.
    """
    file_content = ""
    with open("tests/test_main.py") as file:
        file_content = file.read()

    match = re.search(r"from (.*) import main", file_content)
    if not match:
        print("Failed to match value in test_main.py.")
        return False

    file_content = file_content.replace(match.group(1), package_name, 1)
    with open("tests/test_main.py", "w") as file:
        file.write(file_content)

    return True


def update_readme_md(project_title: str, project_description: str, repo_url: str, repo_name: str) -> bool:
    """Update the project title, description, repository URL, and cd command in README.md.

    Args:
        project_title (str): The new project title.
        project_description (str): The new project description.
        repo_url (str): The new repository URL.
        repo_name (str): The new repository name.

    Returns:
        bool: True if the values were successfully updated, False otherwise.
    """
    file_content = ""
    with open("README.md") as file:
        file_content = file.read()

    title_match = re.search(r"# (.*)", file_content)
    description_match = re.search(r"#.*\n\n(.*)", file_content)
    repo_match = re.search(r"`git clone (.*)`", file_content)
    cd_match = re.search(r"`cd (.*)`", file_content)
    if not title_match or not description_match or not repo_match or not cd_match:
        print("Failed to match values in README.md.")
        return False

    file_content = file_content.replace(title_match.group(1), project_title, 1)
    file_content = file_content.replace(description_match.group(1), project_description, 1)
    file_content = file_content.replace(repo_match.group(1), repo_url, 1)
    file_content = file_content.replace(cd_match.group(1), repo_name, 1)
    with open("README.md", "w") as file:
        file.write(file_content)

    return True


def main():
    print("===== Project Configuration =====")

    author_name = prompt_with_default("Author Name", DEFAULT_AUTHOR_NAME)
    author_email = prompt_with_default("Author Email", DEFAULT_AUTHOR_EMAIL)

    repo_url = prompt_with_default("Repository URL", DEFAULT_REPO_URL)
    repo_name = repo_url.split("/")[-1].replace(".git", "")

    package_name = repo_name.replace("-", "_")
    package_name = prompt_with_default("Package Name", package_name)
    project_title = package_name.replace("_", " ").title()
    project_title = prompt_with_default("Project Title", project_title)
    project_description = prompt_with_default("Project Description", DEFAULT_PROJECT_DESCRIPTION)

    update_pyproject_toml(package_name, project_description, author_name, author_email)
    rename_package(package_name)
    update_test_main_py(package_name)
    update_readme_md(project_title, project_description, repo_url, repo_name)

    print("===== Configuration Complete =====")


if __name__ == "__main__":
    main()
