# waypoint

[![Unit Tests](https://github.com/ChronoInferna/waypoint/actions/workflows/pytest.yml/badge.svg)](https://github.com/ChronoInferna/waypoint/actions/workflows/pytest.yml)

Project 2 for COP3530

---

Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)

## Overview

waypoint is a Python project created as "Project 2" for COP3530. The repository contains code and supporting files for the assignment. The project is implemented entirely in Python.

## Features

- Pure Python implementation
- Clear module/script layout for the Project 2 deliverable
- Minimal, portable dependencies so it runs on standard Python installations
- Unit tests to verify core functionality

## Requirements

- Python 3.8+ (recommended: 3.10 or later)
- uv for installing optional dependencies

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ChronoInferna/waypoint.git
   cd waypoint
   ```

2. Create necessary environment:

   ```bash
   uv sync
   ```

## Usage

Run the script directly (inside waypoint/waypoint):

```bash
uv run main.py
```

Run the website (inside waypoint/web):

```bash
uv run app.py
```

## Testing

Run tests in the main directory:

```bash
uv run pytest
```

## Repository Structure

- `waypoint/` - Source code
- `data/` - Data is small enough to easily include in repo
- `tests/` - Unit tests
- `web/` - Web application code

## Contributing

Contributions and improvements are welcome. Suggested workflow:

1. Clone the main branch
2. Create a feature branch: `git checkout -b <your-feature>`
3. Make your changes and add tests where appropriate
4. Commit and push: `git commit -m "Add feature" && git push origin <your-feature>`
5. Open a pull request with a clear description of changes

Code is automatically formatted using the Black formatter.

