import sympy as sp
from sympy import latex
from fractions import Fraction

"""
Performs Lagrange polynomial interpolation for a given set of data points.

Args:
    x_values (list or numpy.ndarray): Known x data points.
    y_values (list or numpy.ndarray): Corresponding y data points.

Attributes:
    x_values (list or numpy.ndarray): Known x data points.
    y_values (list or numpy.ndarray): Corresponding y data points.
    n (int): Number of data points.
    poly (sympy.Expr): Simplified Lagrange interpolating polynomial.

Methods:
    build_polynomial():
        Constructs the Lagrange interpolating polynomial using the given x and y data points.
        Simplifies the polynomial and displays it in LaTeX format.

    evaluate_roots():
        Evaluates the Lagrange polynomial at each x data point.
        Displays the calculation steps, including the contribution of each term, 
        and confirms if the evaluated values match the corresponding y data points.

    evaluate_at_point(x_sub):
        Evaluates the Lagrange polynomial at a specific point x_sub.
        Args:
            x_sub (float): The x-value where the polynomial is evaluated.
        Returns:
            str: A formatted string with the evaluated value in both decimal 
                 and fractional forms. Example: "f(2) = 3.3333 = 10/3".

    interpolate():
        Performs the complete interpolation process:
        - Constructs the Lagrange polynomial.
        - Evaluates the polynomial at the given x data points.
        - Confirms the interpolation accuracy.

Returns:
    str: A formatted string representing the evaluation process and results,
         showing the polynomial, intermediate calculations, and final results
         with both decimal values and their fractional equivalents.
"""

class Lagrange:
    def __init__(self, x_values, y_values):
        self.x_values = x_values  # Known x data points
        self.y_values = y_values  # Corresponding y data points
        self.n = len(x_values)    # Number of data points
        self.poly = None          # Lagrange polynomial

    def build_polynomial(self):
        x = sp.Symbol("x")
        polynomial_sum = 0

        # Construct the Lagrange interpolating polynomial
        for i in range(self.n):  # Summation
            term = 1
            for j in range(self.n):  # Product
                if i != j:
                    term *= (x - self.x_values[j]) / (self.x_values[i] - self.x_values[j])
            polynomial_term = self.y_values[i] * term
            polynomial_sum += polynomial_term

        self.poly = sp.simplify(polynomial_sum)
        print("\nInterpolating Polynomial:")
        print(f"f(x) = {latex(self.poly)}")  # Display the polynomial in LaTeX format

    def evaluate_roots(self):
        print("\nNow, we evaluate the polynomial at the given roots:")
        x = sp.Symbol("x")
        for xi in self.x_values:
            terms = []  # List to store the terms in string format
            term_values = []  # List to store the evaluated values of each term
            result = 0  # Initialize result to 0

            # Extract each term of the polynomial and replace the 'x' with each value of x_data
            for coef in self.poly.as_ordered_terms():
                if coef.has(x):
                    # Format the term as 'a*(x)^n'
                    term_str = str(coef).replace("x", f"({xi})")  # Replace x with xi
                    term_value = coef.subs(x, xi)  # Calculate the value for each term
                    terms.append(term_str)
                    term_values.append(term_value)
                else:
                    terms.append(str(coef))
                    term_values.append(coef)

            # Join all terms into a string representation
            expression = " + ".join(terms).replace("+ -", "- ")
            simplified_terms = " + ".join(
                [f"{term_value:.2f}" if term_value >= 0 else f"- {abs(term_value):.2f}" for term_value in term_values]
            ).replace("+ -", "- ")

            # Final result after evaluating each term
            result = sum(term_values)
            print(f"f({xi}) = {expression} = {simplified_terms} = {result:.2f}")

            # Confirm if the result matches the corresponding y_value
            if result == self.y_values[self.x_values.index(xi)]:
                print(f"Thus, f({xi}) = {result:.2f} matches y{self.x_values.index(xi)}")

    def evaluate_at_point(self, x_sub):
        y_sub = self.poly.subs(sp.Symbol('x'), x_sub)
        fractional_result = Fraction(float(y_sub)).limit_denominator()
        print(f"f({x_sub}) = {y_sub:.2f} = {fractional_result}")

    def interpolate(self):
        self.build_polynomial()
        self.evaluate_roots()

"""
# Example usage
x_data = [1, 2, 3]
y_data = [3, 1, 5]

lagrange = Lagrange(x_data, y_data)
lagrange.interpolate()
"""
