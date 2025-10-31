# waypoint

[![Run pytest](https://github.com/ChronoInferna/waypoint/actions/workflows/pytest.yml/badge.svg)](https://github.com/ChronoInferna/waypoint/actions/workflows/pytest.yml)

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

This README provides instructions for installing dependencies, running the code, and running tests. If the repository includes multiple modules or scripts, consult the "Repository Structure" section to identify where to run specific components.

## Features

- Pure Python implementation (100% of repository code is Python)
- Clear module/script layout for the Project 2 deliverable
- Minimal, portable dependencies so it runs on standard Python installations
- Unit tests to verify core functionality

## Requirements

- Python 3.8+ (recommended: 3.10 or later)
- uv for installing optional dependencies

## Installation

1. Clone the repository:

   git clone https://github.com/ChronoInferna/waypoint.git
   cd waypoint

2. Create necessary environment:

   uv sync

## Usage

- Run the script directly (inside waypoint/waypoint):

  uv run main.py

## Testing

Run tests in the main directory with uv and pytest:

   uv run pytest

## Repository Structure

- waypoint/                     - Main package / modules (Python source files)
- tests/                        - Unit tests

## Contributing

Contributions and improvements are welcome. Suggested workflow:

1. Fork the repository
2. Create a feature branch: git checkout -b <your-feature>
3. Make your changes and add tests where appropriate
4. Commit and push: git commit -m "Add feature" && git push origin <your-feature>
5. Open a pull request with a clear description of changes

Code is automatically formatted using the Black formatter.
