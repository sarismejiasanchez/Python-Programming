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


"""
Below is a list of commonly used flags and options available in `pytest`, along with brief explanations and 
example usage:

▶ Basic usage:
$ pytest                         # Run all tests in the current directory and subdirectories
$ pytest test_module.py          # Run tests from a specific file
$ pytest test_module.py::TestClass::test_method  # Run a specific test method

▶ Common flags:

--maxfail=N                     # Stop after N failures
$ pytest --maxfail=2

-v / --verbose                  # Show more detailed output
$ pytest -v

-q / --quiet                    # Show less output
$ pytest -q

-x / --exitfirst                # Stop at the first failure
$ pytest -x

--tb=short / line / no         # Control traceback formatting
$ pytest --tb=short

-s                              # Disable output capture (e.g., for debugging print statements)
$ pytest -s

--disable-warnings             # Disable warning messages during test execution
$ pytest --disable-warnings

-k EXPRESSION                  # Run tests that match the given substring expression
$ pytest -k "mean and not median"

-m MARKEXPR                    # Run tests with specific markers
$ pytest -m "slow"

--lf / --last-failed           # Only rerun tests that failed in the last run
$ pytest --lf

--ff                           # Run failed tests first, then the rest
$ pytest --ff

--durations=N                  # Show N slowest test durations
$ pytest --durations=5

--cov=MODULE                   # Measure code coverage using `pytest-cov` plugin
$ pytest --cov=my_module

▶ Test discovery and structure:
- Test files should be named starting with `test_` or ending in `_test.py`
- Test functions should be named starting with `test_`
- You can group tests inside classes prefixed with `Test`

▶ Markers (defined with @pytest.mark.<markername>):
- @pytest.mark.skip
- @pytest.mark.xfail
- @pytest.mark.slow (custom marker; requires registration in pytest.ini)

▶ Configuration:
You can configure pytest behavior using a `pytest.ini`, `pyproject.toml`, or `tox.ini` file.

Example `pytest.ini`:
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
addopts = -ra -q

Note: When working on automation projects or pipelines, you may want to integrate `pytest` with CI/CD tools 
and enable HTML or JUnit reporting using additional plugins like `pytest-html` or `pytest-xdist`.

"""
