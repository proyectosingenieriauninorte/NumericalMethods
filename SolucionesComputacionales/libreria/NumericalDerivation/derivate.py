import numpy as np
import sympy as sp

def derivative(f, a, method, h):
    """
    Computes the numerical derivative of a function at a point using finite differences.

    Args:
        f (callable): The function to differentiate.
        a (float): The point at which to evaluate the derivative.
        method (str): The finite difference method to use ('central', 'forward', or 'backward').
        h (float): The step size for finite differences.

    Returns:
        float: The numerical derivative of f at point a.
    """
    if method == 'central':
        return (f(a + h) - f(a - h))/(2*h)
    elif method == 'forward':
        return (f(a + h) - f(a))/h
    elif method == 'backward':
        return (f(a) - f(a - h))/h
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'.")

"""
#Example:
x = sp.symbols('x')
f_sym =  x**3 + 3*x**2 + x
f = sp.lambdify(x, f_sym, 'numpy')
a=0.5
method='central'
h=0.01
dy_dx_numeric = derivative(f, a,method,h)


print("Numerical Derivative:")
print(dy_dx_numeric)
"""