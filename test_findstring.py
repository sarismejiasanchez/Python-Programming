# APPLY TDD

# 1. Write a test for a feature that fails.
# 2. Write code in accordance with the tests.
# 3. Refactor if code fails.

import findstring
import pytest

# Test para verificar si el nombre está en la lista
def test_ispresent():
    assert findstring.ispresent('John') == True
    assert findstring.ispresent('Alice') == False  # Caso que no está en la lista

# Test para verificar que el valor no sea numérico
def test_nodigit():
    assert findstring.nodigit('Do') == True
    assert findstring.nodigit('123') == False  # Caso numérico

# Test para verificar que el nombre no sea vacío
def test_not_empty():
    assert findstring.not_empty('Jane') == True
    assert findstring.not_empty('') == False  # Caso vacío

# Test para verificar que el nombre no contenga caracteres especiales
def test_no_special_chars():
    assert findstring.no_special_chars('John') == True
    assert findstring.no_special_chars('John0') == False # Caso con dígitos
    assert findstring.no_special_chars('John@') == False  # Caso con caracteres especiales