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

## Why SBOM Matters

An SBOM (Software Bill of Materials) is an inventory of all software dependencies and components used in a project.

SBOMX is useful because it:

- Provides visibility into project dependencies.
- Helps identify security vulnerabilities in components.
- Improves software supply-chain security.
- Can support standardized formats such as SPDX and CycloneDX.

The current version of SBOMX focuses on discovering dependencies and generating the SBOM. Vulnerability detection can be added as a future feature.

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
