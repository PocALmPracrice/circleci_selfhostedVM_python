# tests/test_sample.py

import pytest
from my_app.sample import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
