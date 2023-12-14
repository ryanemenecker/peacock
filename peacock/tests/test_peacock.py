"""
Unit and regression test for the peacock package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import peacock


def test_peacock_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "peacock" in sys.modules
