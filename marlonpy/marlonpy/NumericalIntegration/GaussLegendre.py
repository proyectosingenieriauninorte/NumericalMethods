import sympy as sp
import numpy as np

def gauss_legendre(f, lower_limit, upper_limit, num_points):
    """
    Computes the approximate integral of a function using Gauss-Legendre quadrature.

    Args:
        f (sympy.core.expr.Expr): The function to integrate.
        lower_limit (float): The lower limit of integration.
        upper_limit (float): The upper limit of integration.
        num_points (int): The number of points (nodes) for Gauss-Legendre quadrature.

    Returns:
        tuple: A tuple containing:
            - float: The theoretical value of the integral using symbolic integration.
            - float: The experimental value of the integral using Gauss-Legendre quadrature.
            - float: The absolute error between the experimental and theoretical values.
            - float: The relative error (percentage) between the experimental and theoretical values.
    """
    x = sp.Symbol("x")
    
    #Obtain Gauss-Legendre quadrature points and weights
    nodes, weights = np.polynomial.legendre.leggauss(num_points)
    
    experimental_value = 0.0
    
    #Compute the experimental value using Gauss-Legendre quadrature
    for i in range(num_points):
        point = ((upper_limit - lower_limit) / 2) * nodes[i] + ((lower_limit + upper_limit) / 2)
        value_at_point = f.subs(x, point)
        experimental_value += weights[i] * value_at_point
    
    #Scale the experimental value by 0.5 * (b - a)
    experimental_value *= 0.5 * (upper_limit - lower_limit)
    
    #Calculate the theoretical value of the integral
    theoretical_value = sp.integrate(f, (x, lower_limit, upper_limit)).evalf()
    
    #Calculate absolute and relative errors
    absolute_error = abs(theoretical_value - experimental_value)
    relative_error = abs((theoretical_value - experimental_value) / theoretical_value) * 100
    
    return theoretical_value, experimental_value, absolute_error, relative_error

"""
# Example usage:
x = sp.Symbol("x")
lower_limit = 1/2
upper_limit = 1
num_points = 5
f = sp.cos(sp.sqrt(x + 1)) / sp.log(sp.sqrt(x + 1))

# Compute the integral using Gauss-Legendre quadrature
theoretical_value, experimental_value, absolute_error, relative_error = gauss_legendre(f, lower_limit, upper_limit, num_points)

print("Theoretical Value:", theoretical_value)
print("Experimental Value:", experimental_value)
print("Absolute Error:", absolute_error)
print("Relative Error (%):", relative_error)
"""