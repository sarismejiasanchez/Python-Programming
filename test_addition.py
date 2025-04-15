# TESTS FOR THE ADDITION MODULE USING PYTEST

# This file contains unit tests for the `addition` module using the Pytest framework.
# Pytest is a testing framework that simplifies writing and running test cases.

# Install Pytest:
# pip install pytest

import addition
import pytest

# Test the `add` function from the `addition` module.
def test_add():
    assert addition.add(4, 5) == 9
    assert addition.add(-4, 5) == 1
    assert addition.add(4.5, 5) == 9.5

# Test the `sub` function from the `addition` module.
def test_sub():
    assert addition.sub(5, 4) == 1
    assert addition.sub(4, 5) == -1
    assert addition.sub(4.5, 5) == -0.5

# Executing the tests:
# python -m pytest test_addition.py
# pytest test_addition.py

# Execute test for specific function:
# pytest test_addition.py::test_add
# pytest test_addition.py::test_sub