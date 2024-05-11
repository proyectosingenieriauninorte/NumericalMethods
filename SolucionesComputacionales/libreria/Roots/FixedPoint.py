import sympy as sp

def fixed_point(gx, x0, tol):
    """
     Implementation of the fixed point method to find a root of the function g(x) = x.

     Args:
         gx (sympy.core.expr.Expr): Function g(x) used in the fixed point method.
         x0 (float): Initial approach.
         tol (float): Tolerance for the convergence criterion (default: 1e-2).

     Returns:
         float: Approximation of the root found.
     """
    x = sp.Symbol('x')
    xm = gx.subs(x, x0).evalf()  # Calcular primera aproximación

    while abs(xm - x0) > tol:
        x0 = xm
        xm = gx.subs(x, x0).evalf()  # Siguiente aproximación

    return xm

""""
#Example:
x = sp.Symbol('x')
gx = (2 * sp.exp(x**2)) / 5
x0 = 0
tol = 1e-2
root_approx = fixed_point(gx, x0, tol)
print("La raíz aproximada es:", root_approx)
"""
