
# Triangle Classifier

## Project Description

This project is a triangle classifier created using Python for my Software Engineering assignment. The program takes three side lengths and determines whether they form a valid triangle. If the triangle is valid, it identifies whether it is equilateral, isosceles, or scalene. It also checks whether the triangle has a right angle.

The purpose of this project is to practice Python programming, unit testing, reviewing AI-generated suggestions, and testing software based on customer requirements.

## Files in the Project

- **triangle.py:** Contains the functions that validate and classify triangles.
- **test_triangle.py:** Contains unit tests for different triangle types, invalid inputs, and boundary cases.
- **test_acceptance.py:** Contains an acceptance test based on the stained-glass studio requirements.
- **requirements.txt:** Contains the pytest dependency.
- **README.md:** Explains the project, testing process, and AI usage.

## How to Run the Tests

First, open the repository in GitHub Codespaces.

Install the required package:

```bash
python -m pip install -r requirements.txt
```

Run all the tests:

```bash
python -m pytest -v
```

### Test Results

I ran the tests using pytest in GitHub Codespaces. After correcting the triangle classification bug and adding the boundary tests, all 14 tests passed successfully.

**Final Results: 14 passed in 0.04 seconds.**

## Equivalence Classes and Boundary Cases

I identified different types of inputs to make sure the program correctly classifies triangles and handles invalid side lengths.

| Equivalence Class | Example | Expected Result |
|---|---|---|
| Zero side length | (0, 4, 5) | Invalid |
| Negative side length | (-1, 4, 5) | Invalid |
| Triangle inequality fails | (1, 2, 10) | Invalid |
| Degenerate triangle | (1, 2, 3) | Invalid |
| Equilateral triangle | (5, 5, 5) | Equilateral |
| Isosceles triangle | (5, 5, 6) | Isosceles |
| Scalene triangle | (4, 5, 6) | Scalene |
| Right scalene triangle | (3, 4, 5) | Right Scalene |
| Right isosceles triangle | (5, 5, 5 × √2) | Right Isosceles |
| Right scalene with non-integer sides | (1, √3, 2) | Right Scalene |
| Very small equilateral triangle | (1e-7, 1e-7, 1e-7) | Equilateral |
| Nearly degenerate valid triangle | (2, 3, 4.999999) | Scalene |
| Beyond degenerate boundary | (2, 3, 5.000001) | Invalid |

### Boundary Testing

One important boundary case is when the sum of two sides equals the third side. For example, sides 1, 2, and 3 cannot form a valid triangle because 1 + 2 = 3.

I also tested zero and negative side lengths because a triangle must have three positive sides.

GitHub Copilot suggested three additional boundary tests. These included a very small equilateral triangle, a triangle that is almost degenerate but still valid, and a triangle that is just beyond the valid boundary.

The small equilateral triangle test helped me find a bug in my program. The classifier originally returned "Right Equilateral" instead of "Equilateral." I corrected the code, and the test passed afterward.

For right triangles, the program uses `math.isclose()` instead of directly comparing floating-point calculations with `==`. This helps prevent incorrect results caused by small rounding differences.

## Why an Equilateral Triangle Cannot Be a Right Triangle

An equilateral triangle has three equal angles of 60 degrees. A right triangle must have one angle of 90 degrees, so an equilateral triangle cannot also be a right triangle.

I learned why this matters when I tested a very small equilateral triangle. My program originally classified it as "Right Equilateral," which is mathematically incorrect.

To fix this, I changed the classifier so it returns "Equilateral" immediately when all three sides are equal. This prevents the program from incorrectly checking an equilateral triangle as a right triangle.

## Copilot Review Log

For this assignment, I used GitHub Copilot to review existing triangle tests and suggest additional unit tests. I checked the suggestions to make sure the expected results matched the assignment requirements.

| Test | Copilot-Suggested? | Decision | Explanation |
|---|---|---|---|
| test_invalid_triangle | Not confirmed | Reviewed | Checked that zero and negative side lengths return Invalid. |
| test_degenerate_triangle | No, reviewed by Copilot | Kept | Copilot confirmed that (1, 2, 3) returns Invalid because it does not satisfy the triangle inequality. |
| test_equilateral_triangle | Not confirmed | Reviewed | Checked that three equal sides return Equilateral. |
| test_isosceles_triangle | Not confirmed | Reviewed | Checked that exactly two equal sides return Isosceles. |
| test_scalene_triangle | Not confirmed | Reviewed | Checked that three different sides return Scalene. |
| test_right_triangle | Not confirmed | Reviewed | Checked that (3, 4, 5) returns Right Scalene. |
| test_right_isosceles_triangle | No, reviewed by Copilot | Kept | Copilot confirmed that the existing test correctly expects Right Isosceles. |
| test_right_triangle_with_non_integer_side | Yes | Kept | Copilot suggested testing (1, √3, 2). The expected result was Right Scalene, and the test passed. |
| test_very_small_positive_equilateral_triangle | Yes | Kept | Copilot suggested testing very small positive side lengths. The test exposed a bug where the program returned Right Equilateral instead of Equilateral. I corrected the classifier. |
| test_nearly_degenerate_but_valid_triangle | Yes | Kept | Copilot suggested (2, 3, 4.999999). I checked the expected result and confirmed that the valid triangle was classified as Scalene. |
| test_triangle_just_beyond_degenerate_boundary | Yes | Kept | Copilot suggested (2, 3, 5.000001). I confirmed that the triangle was correctly classified as Invalid. |

### Copilot Testing and Bug Correction

I used GitHub Copilot to help me come up with three additional tests for my triangle classifier. One of the tests checked a very small equilateral triangle. When I ran the test, I noticed that my program returned "Right Equilateral" instead of "Equilateral."

I reviewed my code and realized that the program was checking for a right triangle even when all three sides were equal. I fixed the code so it would correctly identify equilateral triangles. After making the changes, I ran all my tests again, and all 14 passed.

This helped me understand why it is important to review Copilot's suggestions and test my code instead of assuming everything works correctly.

The Copilot-generated test correctly identified the expected result. The mistake was in my program's classification logic, not in Copilot's suggested test. I did not identify a confirmed incorrect Copilot suggestion during this review.

### Code Review and Floating-Point Comparisons

Another important issue I reviewed was how the program identifies right triangles.

Using direct floating-point equality can cause problems because decimal calculations may have small rounding differences. The classifier uses `math.isclose()` to compare the squared side lengths with a tolerance.

I checked a right isosceles triangle with sides 5, 5, and 5 × √2. Copilot confirmed that the existing test correctly checks the classification.

I also reviewed Copilot's suggested test for sides 1, √3, and 2. The expected result was Right Scalene, and the test passed.

## Customer Requirements

The customer is a stained-glass studio that needs a program to identify triangle shapes before creating glass pieces.

The program needs to determine whether three side lengths form a valid triangle, identify the shape, and flag right-angle pieces because they require reinforced corners.

## Acceptance Criteria

### Acceptance Criterion 1: Triangle Validation

When a customer enters three side lengths, the program must return "Invalid" if any side is zero or negative or if the triangle inequality is not satisfied. The program must not crash for these inputs.

### Acceptance Criterion 2: Triangle Classification

For valid triangles, the program must return "Equilateral" when all three sides are equal, "Isosceles" when exactly two sides are equal, and "Scalene" when all three sides are different.

### Acceptance Criterion 3: Right-Angle Identification

When the three side lengths form a right triangle, the program must return a classification beginning with "Right ". This identifies glass pieces that need reinforced corners.

## Acceptance Testing

The `test_acceptance.py` file contains an acceptance test that calls the `classify_triangle()` function using different customer scenarios.

The test checks whether the program correctly handles invalid triangles, identifies valid triangle shapes, and flags right triangles.

The acceptance test passed when I ran pytest in GitHub Codespaces.

An initial acceptance-test example was provided through ChatGPT. The assignment requires the final acceptance test to be independently authored without AI assistance. I still need to verify that my final acceptance test meets this requirement.

## AI-Use Disclosure

I used ChatGPT to help me understand the assignment, create the triangle classifier, prepare reference unit tests, create an example acceptance test, and organize the README documentation.

I used GitHub Copilot to review existing triangle tests and suggest additional unit tests. Copilot suggested a right scalene test using non-integer side lengths and three boundary tests.

I reviewed the suggestions before using them. One of the boundary tests revealed that my program incorrectly classified a very small equilateral triangle as a right equilateral triangle. I corrected the classification logic and tested the program again.

I used pytest in GitHub Codespaces to verify the results. All 14 tests passed successfully.

## Conclusion

This project helped me understand how triangle classification works and why testing is important in software development. I learned how to check different inputs, test boundary cases, and verify that a program produces the expected results.

One of the most useful parts of this assignment was finding and correcting the small equilateral triangle bug. It showed me that even when most tests pass, a program can still have problems with certain inputs.

I also learned that AI-generated suggestions need to be reviewed carefully instead of automatically accepting everything.
