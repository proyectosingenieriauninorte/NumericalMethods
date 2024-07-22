import sympy as sp

def runge_kutta(f, x0, y0, h, n):
    """
    Perform the fourth-order Runge-Kutta method to solve a differential equation.

    Args:
        f (sympy.core.expr.Expr): The function representing dy/dx = f(x, y).
        x0 (float): Initial x-value.
        y0 (float): Initial y-value (corresponding to f(x0)).
        h (float): Step size.
        n (int): Number of iterations.

    Returns:
        tuple: Two lists containing the x and y values at each step.
    """
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    # Lists to store x and y values
    x_values = [x0]
    y_values = [y0]

    print(f"{'   k1   ':<5} {' k2':<5} {' k3  ':<5} {'  k4':<5}{'   x ':<5} {'   y':<5}")

    for i in range(n):
        k1 = f.subs([(x, x0), (y, y0)])
        k2 = f.subs([(x, x0 + h / 2), (y, y0 + k1 * h / 2)])
        k3 = f.subs([(x, x0 + h / 2), (y, y0 + k2 * h / 2)])
        k4 = f.subs([(x, x0 + h), (y, y0 + k3 * h)])
        
        yi = y0 + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
        x0 = x0 + h
        y0 = yi
        
        x_values.append(x0)
        y_values.append(yi)
        
        print(f"{k1.evalf():<5.4f} {k2.evalf():<5.4f} {k3.evalf():<5.4f} {k4.evalf():<5.4f} {x0:<5.4f} {yi:<5.4f}")
    
    return x_values, y_values

"""
#Example usage:
x = sp.Symbol('x')
y = sp.Symbol('y')
f = x * sp.sqrt(y)

# Initial conditions
x0 = 1
y0 = 4

# Step size and number of iterations
h = 0.2
n = 3

# Use the runge_kutta function to solve the differential equation
x_values, y_values = runge_kutta(f, x0, y0, h, n)
"""
