import pytest
from app import calculate


def test_addition():
    assert calculate(10, 5, "add") == 15


def test_subtraction():
    assert calculate(10, 5, "subtract") == 5


def test_multiplication():
    assert calculate(10, 5, "multiply") == 50


def test_division():
    assert calculate(10, 5, "divide") == 2


def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculate(10, 0, "divide")


def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation"):
        calculate(10, 5, "invalid")
