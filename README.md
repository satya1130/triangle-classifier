
# Triangle Classifier

## Project Description

This project is a triangle classifier written in Python. It takes three side lengths and determines whether they form a valid triangle. If the triangle is valid, the program classifies it as equilateral, isosceles, or scalene. It also identifies right triangles.

## How to Run the Tests

Install pytest:

```bash
python -m pip install -r requirements.txt
```

Run all tests:

```bash
python -m pytest -v
```

## Equivalence Classes and Boundaries

The following cases were identified:

1. Invalid triangles with zero or negative sides.
2. Invalid triangles that fail the triangle inequality.
3. Degenerate triangles where two sides add up to the third.
4. Equilateral triangles with three equal sides.
5. Isosceles triangles with exactly two equal sides.
6. Scalene triangles with three different sides.
7. Right triangles that satisfy the Pythagorean theorem.

The boundary cases include zero side lengths and triangles where the sum of two sides equals the third side.

## Why Equilateral Triangles Cannot Be Right Triangles

An equilateral triangle has three angles of 60 degrees. A right triangle must have one 90-degree angle, so an equilateral triangle cannot be a right triangle.

## Copilot Review Log

Complete this table using the suggestions you actually receive from GitHub Copilot.

| Test | Copilot-suggested? | Kept / Edited / Rejected | Why |
|---|---|---|---|
| test_invalid_triangle | | | |
| test_degenerate_triangle | | | |
| test_equilateral_triangle | | | |
| test_isosceles_triangle | | | |
| test_scalene_triangle | | | |
| test_right_triangle | | | |
| test_right_isosceles_triangle | | | |

## Acceptance Criteria

1. The program returns "Invalid" for zero, negative, or degenerate side lengths without crashing.
2. Valid triangles are classified as "Equilateral", "Isosceles", or "Scalene" based on their side lengths.
3. Valid right triangles have "Right " at the beginning of their classification to identify pieces requiring reinforced corners.

## AI-Use Disclosure

GitHub Copilot: [Describe the actual unit test suggestions received, which were accepted or edited, and what was checked.]

ChatGPT: Used for reference implementation code, example tests, and README drafting.

Verification: [Describe the tests run and the results you personally verified.]

Acceptance test: [Describe how you independently wrote this test without Copilot, as required.]
