
import math
import pytest

from triangle import classify_triangle, is_valid_triangle


def test_invalid_triangle():
    assert classify_triangle(0, 4, 5) == "Invalid"
    assert classify_triangle(-1, 4, 5) == "Invalid"
    assert classify_triangle(1, 2, 10) == "Invalid"


def test_degenerate_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(5, 5, 10) == "Invalid"


def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(5, 5, 6) == "Isosceles"


def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_right_isosceles_triangle():
    result = classify_triangle(5, 5, 5 * math.sqrt(2))
    assert result == "Right Isosceles"


def test_valid_triangle():
    assert is_valid_triangle(3, 4, 5) is True
    assert is_valid_triangle(1, 2, 3) is False


def test_right_triangle_side_order():
    assert classify_triangle(5, 3, 4) == "Right Scalene"
    assert classify_triangle(4, 5, 3) == "Right Scalene"


def test_right_triangle_with_non_integer_side():
    assert classify_triangle(1, math.sqrt(3), 2) == "Right Scalene"
