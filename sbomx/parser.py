import tomllib
from pathlib import Path

def parse_pyproject(project_path):
    project = Path(project_path)
    pyproject_file = project / "pyproject.toml"

    with pyproject_file.open("rb") as file:
        data = tomllib.load(file)

    project_data = data.get("project", {})
    dependencies = project_data.get("dependencies", [])

    return dependencies

