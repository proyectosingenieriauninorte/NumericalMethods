import sympy as sp

def trapezoidal(f, num_intervals, lower_limit, upper_limit, step_size):
    """
    Computes the approximate integral of a function using the Trapezoidal rule.

    Args:
        f (sympy.core.expr.Expr): The function to integrate.
        num_intervals (int): The number of intervals (subdivisions) for the Trapezoidal rule.
        lower_limit (float): The lower limit of integration.
        upper_limit (float): The upper limit of integration.
        step_size (float): The width of each interval (step size).

    Returns:
        tuple: A tuple containing:
            - float: The experimental value of the integral using the Trapezoidal rule.
            - float: The theoretical value of the integral using symbolic integration.
            - float: The absolute error between the experimental and theoretical values.
            - float: The relative error (percentage) between the experimental and theoretical values.
            - float: The error estimate using the Trapezoidal rule formula.
    """
    x = sp.Symbol("x")
    
    #Calculate f(lower_limit) and f(upper_limit)
    sum_terms = f.subs(x, lower_limit) + f.subs(x, upper_limit)
    
    #Calculate intermediate values
    for k in range(1, num_intervals):
        sum_terms += 2 * f.subs(x, lower_limit + k * step_size)

    experimental_value = (sum_terms * step_size / 2).evalf()
    theoretical_value = sp.integrate(f, (x, lower_limit, upper_limit)).evalf()
    absolute_error = abs(theoretical_value - experimental_value)
    relative_error = abs(theoretical_value - experimental_value) / theoretical_value
    
    #Compute second derivative of f
    f_second_derivative = sp.diff(f, x, 2)
    
    #Calculate error estimate using Trapezoidal rule formula
    error_estimate = float(abs(-(upper_limit - lower_limit)**3 / (12 * num_intervals**2) * max(f_second_derivative.subs(x, lower_limit), f_second_derivative.subs(x, upper_limit))))
     
    return experimental_value, theoretical_value, absolute_error, relative_error, error_estimate


"""
#Example:
x = sp.Symbol("x")
f = sp.sin(sp.sqrt(x)) / sp.exp(3 * x + sp.sqrt(x))
num_intervals = 9  #number of intervals -> n
lower_limit = 1  #lower limit -> a
upper_limit = 3  #upper limit -> b
step_size = (upper_limit - lower_limit) / num_intervals #h =(b-a)/n

#Call the trapezoidal function to compute the integral approximation and errors
experimental_value, theoretical_value, absolute_error, relative_error, error_estimate = trapezoidal(f, num_intervals, lower_limit, upper_limit, step_size)

print("Experimental Value (lastsum*h/2):", experimental_value)
print("Theoretical Value:", theoretical_value)
print("Relative Error:", relative_error)
print("Absolute Error:", absolute_error)
print("Error Estimate (Formula):", error_estimate)
"""