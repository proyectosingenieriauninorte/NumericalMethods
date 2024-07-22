import sympy as sp

def Simpson_3_8(f, lower_limit, upper_limit, num_intervals):
    """
    Computes the approximate integral of a function using Simpson's 3/8 rule.

    Args:
        f (sympy.core.expr.Expr): The function to integrate.
        lower_limit (float): The lower limit of integration.
        upper_limit (float): The upper limit of integration.
        num_intervals (int): The number of intervals (subdivisions) for Simpson's 3/8 rule.

    Returns:
        tuple: A tuple containing:
            - float: The experimental value of the integral using Simpson's 3/8 rule.
            - float: The theoretical value of the integral using symbolic integration.
            - float: The absolute error between the experimental and theoretical values.
            - float: The relative error (percentage) between the experimental and theoretical values.
    """
    #Calculate the step size (h) for each subinterval
    h = (upper_limit - lower_limit) / num_intervals

    #Initialize the sum with the values at the endpoints (f(a) and f(b))
    sum_terms = f.subs(sp.Symbol('x'), lower_limit) + f.subs(sp.Symbol('x'), upper_limit)

    #Calculate intermediate values using Simpson's 3/8 rule
    for i in range(1, num_intervals):
        if i % 3 == 0:
            sum_terms += 2 * f.subs(sp.Symbol('x'), lower_limit + i * h)
        else:
            sum_terms += 3 * f.subs(sp.Symbol('x'), lower_limit + i * h)

    #Calculate the experimental value using Simpson's 3/8 rule formula
    experimental_value = float((3/8) * sum_terms * h)

    #Calculate the theoretical value of the integral
    theoretical_value = float(sp.integrate(f, (sp.Symbol('x'), lower_limit, upper_limit)))

    #Calculate absolute error (Ea) and relative error (Er)
    absolute_error = abs(theoretical_value - experimental_value)
    relative_error = abs((theoretical_value - experimental_value) / theoretical_value) * 100

    return experimental_value, theoretical_value, absolute_error, relative_error

"""
#Example:
x = sp.Symbol('x')
f = (sp.cos(sp.sqrt(x))) / (sp.exp(x + sp.sqrt(x)))
lower_limit = 1 
upper_limit = 3
num_intervals = 9

#Call the Simpson_3_8 function to compute the integral approximation and errors
experimental_value, theoretical_value, absolute_error, relative_error = Simpson_3_8(f, lower_limit, upper_limit, num_intervals)

print("Experimental Value (Simpson's 3/8 rule):", experimental_value)
print("Theoretical Value:", theoretical_value)
print("Absolute Error (Ea):", absolute_error)
print("Relative Error (Er):", relative_error, "%")
"""