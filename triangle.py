
import math


def is_valid_triangle(a, b, c) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False

    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return True


def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        return "Equilateral"

    if a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    sides = sorted([a, b, c])

    largest = sides[2]
    x = sides[0] / largest
    y = sides[1] / largest

    if math.isclose(
        x ** 2 + y ** 2,
        1.0,
        rel_tol=1e-9,
        abs_tol=1e-12
    ):
        return "Right " + triangle_type

    return triangle_type
