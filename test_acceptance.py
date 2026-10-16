
from triangle import classify_triangle


def test_stained_glass_customer_requirements():
    # Check that invalid measurements are rejected
    assert classify_triangle(0, 4, 5) == "Invalid"
    assert classify_triangle(1, 2, 3) == "Invalid"

    # Check that the studio can identify triangle shapes
    assert classify_triangle(6, 6, 6) == "Equilateral"
    assert classify_triangle(7, 7, 9) == "Isosceles"
    assert classify_triangle(5, 6, 7) == "Scalene"

    # Check right-angle pieces that need reinforced corners
    assert classify_triangle(6, 8, 10) == "Right Scalene"
    assert classify_triangle(5, 5, 5 * (2 ** 0.5)) == "Right Isosceles"
