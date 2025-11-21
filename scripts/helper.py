#!/usr/bin/env python3
"""Helper script for common tasks."""

import sys
from pathlib import Path

def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent

if __name__ == "__main__":
    print(f"Project root: {get_project_root()}")

