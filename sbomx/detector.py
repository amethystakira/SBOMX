from pathlib import Path

def detect_ecosystem(project_path):
    project = Path(project_path)

    manifests = []


    if (project / "requirements.txt").exists():
        manifests.append("requirements.txt")
    if (project / "pyproject.toml").exists():
        manifests.append("pyhton")
    if (project/ "package.json").exists():
        manifests.append("node")

    if not manifests:
        return {
            "ecosystem" : "unknown",
            "manifests" : []
        }
    
    if "package.json" in manifests:
        ecosystem = "node"
    else:
        ecosystem = "python"


    return {
        "ecosystem" : ecosystem,
        "manifests" : manifests
    }