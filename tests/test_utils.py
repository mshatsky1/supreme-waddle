"""Tests for utils module."""

from utils import greet


def test_greet():
    """Test the greet function."""
    assert greet("World") == "Hello, World!"
    assert greet("Alice") == "Hello, Alice!"

