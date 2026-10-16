
# Triangle Classifier

## Project Description

This project is a triangle classifier created using Python for my Software Engineering assignment. The program takes three side lengths and checks whether they form a valid triangle. If the triangle is valid, it determines whether it is equilateral, isosceles, or scalene. It also checks if the triangle has a right angle.

The purpose of this project is to practice Python programming, unit testing, boundary testing, and reviewing AI-generated suggestions.

## Files in the Project

- **triangle.py:** Contains the functions used to validate and classify triangles.
- **test_triangle.py:** Contains unit tests for triangle classification and boundary cases.
- **test_acceptance.py:** Contains an acceptance test based on customer requirements.
- **requirements.txt:** Contains the pytest dependency.
- **README.md:** Explains the project, testing process, and AI usage.

## How to Run the Tests

Open the repository in GitHub Codespaces.

Install pytest:

```bash
python -m pip install -r requirements.txt
```

Run the tests:

```bash
python -m pytest -v
```

## Test Results

Before making the latest changes, I ran the test suite in GitHub Codespaces and all 14 tests passed.

After reviewing Copilot's suggestions, I updated the right-triangle calculation to handle very small side lengths more accurately.

The updated version needs to be tested again to confirm that all tests still pass.

## Equivalence Classes and Boundary Cases

I identified different types of inputs to check whether the program correctly classifies triangles and handles invalid values.

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
| Non-integer right triangle | (1, √3, 2) | Right Scalene |
| Very small equilateral | (1e-7, 1e-7, 1e-7) | Equilateral |
| Very small isosceles | (1e-7, 1e-7, 1.5e-7) | Isosceles |
| Very small right scalene | (3e-7, 4e-7, 5e-7) | Right Scalene |
| Nearly degenerate valid triangle | (2, 3, 4.999999) | Scalene |
| Beyond degenerate boundary | (2, 3, 5.000001) | Invalid |
| Near-right triangle | (3, 4, 5.0000001) | Scalene |

### Boundary Testing

One important boundary case is when the sum of two sides equals the third side. For example, sides 1, 2, and 3 cannot form a valid triangle because 1 + 2 = 3.

I also tested zero and negative side lengths because triangles must have three positive sides.

GitHub Copilot suggested additional boundary tests, including very small triangles and triangles that are close to being invalid.

These tests helped me find problems that were not covered by my original tests.

## Triangle Classification

The program uses two functions.

### is_valid_triangle()

This function checks whether the side lengths are positive and satisfy the triangle inequality.

If the sides do not form a valid triangle, the function returns False.

### classify_triangle()

This function identifies the triangle type.

- Equilateral: All three sides are equal.
- Isosceles: Exactly two sides are equal.
- Scalene: All three sides are different.
- Right Isosceles: Two equal sides with a right angle.
- Right Scalene: Three different sides with a right angle.
- Invalid: The sides do not form a triangle.

## Why an Equilateral Triangle Cannot Be a Right Triangle

An equilateral triangle has three equal angles of 60 degrees. A right triangle has one angle of 90 degrees.

Because of this, an equilateral triangle cannot also be a right triangle.

I discovered a problem when my program incorrectly returned "Right Equilateral" for very small equal side lengths.

I corrected the program so it returns "Equilateral" immediately when all three sides are equal.

## Copilot Review Log

For this assignment, I used GitHub Copilot to review existing tests and suggest additional test cases.

I reviewed the suggestions to check whether they matched the assignment requirements.

| Test | Copilot-Suggested? | Decision | Explanation |
|---|---|---|---|
| Invalid triangle | Not confirmed | Reviewed | Checked that invalid side lengths return Invalid. |
| Degenerate triangle | Reviewed by Copilot | Kept | Confirmed that sides (1, 2, 3) cannot form a triangle. |
| Equilateral triangle | Not confirmed | Reviewed | Checked that three equal sides return Equilateral. |
| Isosceles triangle | Not confirmed | Reviewed | Checked that two equal sides return Isosceles. |
| Scalene triangle | Not confirmed | Reviewed | Checked that three different sides return Scalene. |
| Right scalene triangle | Not confirmed | Reviewed | Checked that (3, 4, 5) returns Right Scalene. |
| Right isosceles triangle | Reviewed by Copilot | Kept | Confirmed the expected result was correct. |
| Non-integer right triangle | Yes | Kept | Copilot suggested (1, √3, 2), which should return Right Scalene. |
| Very small equilateral triangle | Yes | Kept | Helped identify a bug in my original classifier. |
| Nearly degenerate valid triangle | Yes | Kept | Checked that (2, 3, 4.999999) returns Scalene. |
| Beyond degenerate boundary | Yes | Kept | Checked that (2, 3, 5.000001) returns Invalid. |
| Very small right scalene triangle | Yes | Reviewed | Checked the expected Right Scalene classification. |
| Near-right triangle | Yes | Reviewed | Checked that (3, 4, 5.0000001) should return Scalene. |

### Copilot Mistake and Correction

While reviewing additional test cases, I noticed that GitHub Copilot incorrectly predicted that my very small equilateral triangle test would fail.

I had already fixed the classifier so it returned "Equilateral" immediately when all three sides were equal.

When I asked Copilot to review its explanation, it acknowledged that it had overlooked my updated code.

This was a mistake in Copilot's explanation because it was using information from an older version of my program.

I reviewed the explanation and corrected the misunderstanding by showing Copilot that the updated classifier already handled equilateral triangles correctly.

This experience helped me understand why it is important to check AI-generated explanations instead of assuming they are always accurate.

### Additional Bug Found During Review

Copilot also helped me identify another problem with my program.

The classifier originally used `math.isclose()` with an absolute tolerance of `1e-12` when comparing squared side lengths.

For very small triangles, this tolerance could incorrectly identify a non-right triangle as a right triangle.

For example, sides (1e-7, 1e-7, 1.5e-7) form a valid isosceles triangle, but the earlier classifier returned "Right Isosceles."

To correct this problem, I updated the code to divide the side lengths by the largest side before checking for a right angle.

This allows the right-angle comparison to work more consistently with triangles of different sizes.

### What I Learned From Copilot

I learned that GitHub Copilot can be helpful for suggesting tests and identifying possible problems, but its suggestions still need to be reviewed.

Copilot made an incorrect prediction about my updated classifier, and reviewing that explanation helped me understand the importance of checking the actual code.

I also learned that testing small numbers and boundary cases can reveal problems that regular test cases might miss.

## Customer Requirements

The customer is a stained-glass studio that needs a program to identify triangle shapes before creating glass pieces.

The program must determine whether three side lengths form a valid triangle, identify the shape, and flag right-angle pieces because they require reinforced corners.

## Acceptance Criteria

### Acceptance Criterion 1: Triangle Validation

When a customer enters three side lengths, the program must return "Invalid" if any side is zero or negative or if the triangle inequality is not satisfied.

### Acceptance Criterion 2: Triangle Classification

For valid triangles, the program must identify whether the triangle is equilateral, isosceles, or scalene.

### Acceptance Criterion 3: Right-Angle Identification

When the side lengths form a right triangle, the program must return a classification beginning with "Right ".

This identifies glass pieces that require reinforced corners.

## Acceptance Testing

The `test_acceptance.py` file contains an acceptance test based on the stained-glass studio's requirements.

The test checks whether the program correctly handles invalid triangles, identifies valid triangle shapes, and flags right triangles.

The acceptance test passed during the previous test run.

An initial acceptance-test example was provided through ChatGPT. The assignment requires the final acceptance test to be independently written without AI assistance, so this requirement still needs to be completed or verified.

## AI-Use Disclosure

I used ChatGPT to help me understand the assignment, prepare the Python classifier, review testing results, correct bugs, and organize the README documentation.

I used GitHub Copilot to review existing triangle tests and suggest additional unit tests.

Copilot helped me identify boundary cases involving very small triangles and triangles close to the triangle inequality boundary.

I reviewed Copilot's explanations and identified an incorrect prediction about the updated equilateral triangle logic.

I also used Copilot's feedback to understand the problem with absolute tolerance in the right-angle calculation.

The final code was updated to normalize side lengths before checking for right angles.

## Conclusion

This project helped me understand how triangle classification works and why software testing is important.

I learned how to identify valid and invalid triangles, check boundary cases, and test different types of inputs.

One of the most useful parts of the assignment was discovering that very small side lengths could cause incorrect results.

I also learned that AI tools can make mistakes, so it is important to review their suggestions carefully and test the code instead of accepting everything automatically.
