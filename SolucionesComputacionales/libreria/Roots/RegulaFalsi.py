import sympy as sp

def regula_falsi(f, a, b, tol=1e-3):
    """
    Implementation of the secant method to find a root of the function f in the interval [a, b].
    
     Args:
         f (sympy.core.expr.Expr): The function of which you want to find the root.
         a (float): Left end of the initial interval.
         b (float): Right end of the initial interval.
         tol (float): Tolerance, stopping criterion based on the absolute value of f(xm) (default: 1e-3).
        
     Returns:
         float: Approximation of the root of f.
     """
    x = sp.Symbol('x')
    fa = f.subs(x, a).evalf()
    fb = f.subs(x, b).evalf()
    
    xm = (a * fb - b * fa) / (fb - fa)
    fxm = f.subs(x, xm).evalf()
    
    while abs(fxm) > tol:
        if fa * fxm > 0:
            a = xm
            fa = f.subs(x, a).evalf()
        elif fa * fxm < 0:
            b = xm
            fb = f.subs(x, b).evalf()

        xm = (a * fb - b * fa) / (fb - fa)
        fxm = f.subs(x, xm).evalf()

    return xm

""""
#Example:
x = sp.Symbol('x')
f = sp.sec(sp.exp(sp.sqrt(x + 1))) - 3
a = 3
b = 3.1
tol = 1e-3
root_approx = regula_falsi(f, a, b, tol)
print("La raíz es:", root_approx)
"""

