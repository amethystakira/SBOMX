from pathlib import Path

from .component import Component
from .detector import detect_ecosystem
from .parser import parse_package_json, parse_pyproject,parse_requirements
from .sbom import SBOM


def scan_project(project_path):
    # Convert the supplied path into a Path object so we can
    # easily perform filesystem checks.
    project = Path(project_path)

    # make sure the supplied path exists
    if not project.exists():
        raise FileNotFoundError(f"Project not found: {project}")
    
    # Make sure the supplied path is a directory
    if not project.is_dir():
        raise NotADirectoryError(f"Not a directory: {project}")


    #detect the project ecosystem
    detection = detect_ecosystem(project)
    ecosystem = detection["ecosystem"]

    sbom = SBOM()

    # parse python project dependencies

    if ecosystem == "python":
        if (project / "pyproject.toml").exists():
            dependencies = parse_pyproject(project)
        elif (project / "requirements.txt").exists():
            dependencies = parse_requirements(project)
        else:
            dependencies = []
    
    # parse node.js project dependencies
    elif ecosystem == "node":
        dependencies = parse_package_json(project)
    
    # return an empty sbom for unsupported ecosysyten
    else:
        dependencies= []
    
    # convert parsed dependencies into sbom components.
    for dependency in dependencies:
        component = Component.from_dependency(dependency, ecosystem)
        sbom.add_component(component)
    
    return sbom
    