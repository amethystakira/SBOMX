from pathlib import Path


def detect_ecosystem(project_path):
    # Convert the supplied project path into a Path object.
    # Path gives us convenient methods for working with
    # files and directories.
    project = Path(project_path)

    # Store the dependency/manifest files found in the project.
    # A project may contain more than one supported manifest.
    manifests = []

    # requirements.txt is a common dependency file for Python projects.
    if (project / "requirements.txt").exists():
        manifests.append("requirements.txt")

    # pyproject.toml is the modern Python project configuration
    # and dependency-management file.
    if (project / "pyproject.toml").exists():
        manifests.append("pyproject.toml")

    # package.json is the main manifest used by Node.js/npm projects.
    if (project / "package.json").exists():
        manifests.append("package.json")

    # If we did not find any supported manifest,
    # SBOMX cannot currently determine the ecosystem.
    if not manifests:
        return {
            "ecosystem": "unknown",
            "manifests": []
        }

    # If package.json exists, classify the project as Node.js.
    # This check is performed before the Python fallback because
    # a project could contain multiple manifest types.
    if "package.json" in manifests:
        ecosystem = "node"
    else:
        # If package.json was not found but a Python manifest was,
        # classify the project as Python.
        ecosystem = "python"

    # Return both the detected ecosystem and the files
    # that caused the detection.
    return {
        "ecosystem": ecosystem,
        "manifests": manifests
    }