#!/usr/bin/env python3
"""Main entry point for the application."""

import argparse

def main() -> None:
    """Main function with argument parsing."""
    parser = argparse.ArgumentParser(description="Supreme Waddle - A simple Python project")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args()
    
    try:
        print(f"Hello, {args.name}!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

