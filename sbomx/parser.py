import re
import tomllib
from pathlib import Path

def parse_dependency(dependency):
    match = re.match(r"^([A-Za-z0-9_.-]+)\s*([<>=!~]+)?\s*(.*)$", dependency)
    if not match:
        return{
            "name" : dependency,
            "operator" : "",
            "version" : ""
        }
    
    name,operator, version = match.groups()

    return {
        "name" : name,
        "operator" : operator or "",
        "version" : version
    }

def parse_pyproject(project_path):
    project = Path(project_path)
    pyproject_file = project / "pyproject.toml"

    with pyproject_file.open("rb") as file:
        data = tomllib.load(file)

    project_data = data.get("project", {})
    dependencies = project_data.get("dependencies", [])

    return dependencies

