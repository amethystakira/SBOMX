from pathlib import Path


def scan_project(project_path):
    project = Path(project_path)

    if not project.exists():
        raise FileNotFoundError(f"Project not found: {project}")

    if not project.is_dir():
        raise NotADirectoryError(f"Not a directory: {project}")

    return project