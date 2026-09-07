from pathlib import Path

def detect_ecosystem(project_path):
    project = Path(project_path)

    if (project / "requirements.txt").exists():
        return "python"
    if (project / "pyproject.toml").exists():
        return "python"
    return "unknown"