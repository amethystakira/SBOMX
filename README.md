# SBOMX

A lightweight terminal application that generates a Software Bill of Materials (SBOM) by discovering project dependencies.

## Features

- Detects Python and Node.js projects.
- Reads dependencies from `pyproject.toml`, `requirements.txt`, and `package.json`.
- Converts dependencies into structured SBOM components.
- Exports the SBOM as JSON.
- Provides a simple terminal interface.
- Validates project paths.
- Displays the number of discovered components.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/amethystakira/SBOMX.git
cd SBOMX
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install SBOMX

```bash
pip install -e .
```

### 4. Verify the installation

```bash
sbomx --help
```

## Usage

### Scan a project

```bash
sbomx /path/to/project
```

### Specify an output file

```bash
sbomx /path/to/project -o sbom.json
```


### Example SBOM Output

```json
{
  "components": [
    {
      "name": "requests",
      "version": "2.31",
      "ecosystem": "python"
    },
    {
      "name": "click",
      "version": "8.1.7",
      "ecosystem": "python"
    }
  ]
}
```

## Project Structure

SBOMX/
├── sbomx/
│ ├── cli.py
│ ├── component.py
│ ├── detector.py
│ ├── parser.py
│ ├── sbom.py
│ └── scanner.py
├── .gitignore
├── pyproject.toml
└── README.md


## How It Works

Project
↓
Ecosystem Detection
↓
Dependency Parsing
↓
Component Creation
↓
SBOM Generation
↓
JSON Export


## Current Status

Basic SBOM generation is implemented for Python and Node.js projects.

## Future Improvements

- [ ] Dependency version resolution
- [ ] Vulnerability detection
- [ ] Support for additional ecosystems
- [ ] Standard SBOM formats such as SPDX and CycloneDX
- [ ] Improved dependency metadata
- [ ] Richer CLI output
