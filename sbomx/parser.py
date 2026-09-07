import re
import tomllib
from pathlib import Path


def parse_dependency(dependency):
    # Use a regular expression to separate a dependency into:
    # package name, version operator, and version constraint.
    #
    # Example:
    #     "requests>=2.31"
    #
    # becomes:
    #     name     = "requests"
    #     operator = ">="
    #     version  = "2.31"
    match = re.match(
        r"^([A-Za-z0-9_.-]+)\s*([<>=!~]+)?\s*(.*)$",
        dependency
    )

    # If the dependency does not match our expected format,
    # preserve the original value instead of crashing.
    if not match:
        return {
            "name": dependency,
            "operator": "",
            "version": ""
        }

    # Extract the three parts captured by the regular expression.
    name, operator, version = match.groups()

    # Return structured dependency information.
    # Structured data will make it easier to resolve versions
    # and generate SBOM components later.
    return {
        "name": name,
        "operator": operator or "",
        "version": version
    }


def parse_pyproject(project_path):
    # Convert the supplied project path into a Path object.
    project = Path(project_path)

    # Build the path to the project's pyproject.toml file.
    pyproject_file = project / "pyproject.toml"

    # Open the TOML file in binary mode.
    # tomllib.load() expects a binary file object.
    with pyproject_file.open("rb") as file:
        # Parse the TOML document into a Python dictionary.
        data = tomllib.load(file)

    # Get the [project] section.
    # If the section does not exist, use an empty dictionary.
    project_data = data.get("project", {})

    # Get the dependency list from [project].
    # If dependencies are not defined, use an empty list.
    dependencies = project_data.get("dependencies", [])

    # Convert every dependency into structured data.
    return [parse_dependency(dependency) for dependency in dependencies]