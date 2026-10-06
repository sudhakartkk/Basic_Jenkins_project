import example
import pytest

def test_average():
    assert example.average([1, 2, 3, 4, 5]) == 3

def test_math_negative():
    assert example.average([]) == 0