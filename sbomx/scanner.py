from pathlib import Path


def scan_project(project_path):
    # Convert the supplied path into a Path object so we can
    # easily perform filesystem checks.
    project = Path(project_path)

    # Make sure the supplied path actually exists.
    # Scanning a path that does not exist would otherwise
    # produce confusing errors later.
    if not project.exists():
        raise FileNotFoundError(f"Project not found: {project}")

    # Make sure the path points to a directory rather than
    # an individual file.
    if not project.is_dir():
        raise NotADirectoryError(f"Not a directory: {project}")

    # Return the validated project path.
    #
    # Later this function will become the starting point
    # for the complete SBOM scanning pipeline.
    return project