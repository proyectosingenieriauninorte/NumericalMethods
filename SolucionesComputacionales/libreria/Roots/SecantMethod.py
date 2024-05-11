import sympy as sp

def secant_method(f, a, b, tol):
    """
    Find a root of the function f in the interval [a, b] using the secant method.

    Args:
        f (sympy.core.expr.Expr): The function for which to find the root.
        a (float): Left endpoint of the interval.
        b (float): Right endpoint of the interval.
        tol (float): Tolerance for the convergence of the method.

    Returns:
        float or None: Approximation of the root found, or None if the initial condition is not met.
    """
    x = sp.Symbol("x")
    fa = f.subs(x, a).evalf()
    fb = f.subs(x, b).evalf()
    
    while abs(fb) > tol:
        xm = (a * fb - b * fa) / (fb - fa)
        a = b
        b = xm
        fa = f.subs(x, a).evalf()
        fb = f.subs(x, b).evalf()
        
    return b if abs(fb) <= tol else None

"""
#Example:
x = sp.Symbol("x")
f = x**3 - sp.cos(x)
a = 0
b = 1
tol = 1e-3

root = secant_method(f, a, b, tol)
if root is not None:
    print("Approximate root found:", root)
else:
    print("The secant method did not converge to a root within the tolerance.")
"""
