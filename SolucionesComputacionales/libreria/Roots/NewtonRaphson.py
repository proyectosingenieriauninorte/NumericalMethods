import sympy as sp

def newton_raphson(f, x0, tol):

    """
     Find a root of the function f using the Newton-Raphson method.

     Args:
         f (sympy.core.expr.Expr): The function for which the root is searched.
         x0 (float): Initial value to start the method.
         tol (float): Tolerance for the convergence of the method.

     Returns:
         float: Approximation of the root found.
     """
    x = sp.Symbol("x")
    fxi = f.subs(x, x0)
    
    while abs(fxi) > tol:
        f_prime = sp.diff(f, x)
        x_sig = x0 - fxi / f_prime.subs(x, x0)
        x0 = x_sig
        fxi = f.subs(x, x0)
    
    return x0.evalf()

""" 
#Example:
x = sp.Symbol("x")
f = sp.log(sp.sqrt((x**2 + 1) / (1 + x)))
x0 = 0.3
tol = 1e-7

raiz_aprox = newton_raphson(f, x0, tol)

print("La raíz aproximada es:", raiz_aprox)
"""