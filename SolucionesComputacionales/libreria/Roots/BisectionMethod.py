import sympy as sp

def bisection_method(f, a, b, tol):
    """
     Find a root of the function f on the interval [a, b] using the bisection method.
    
     Args:
         f (sympy.core.expr.Expr): The function for which the root is searched.
         a (float): Left end of the interval.
         b (float): Right end of the interval.
         tol (float): Tolerance for the convergence of the method.
        
     Returns:
         float or None: Approximation of the root found, or None if the initial condition is not met.
     """
    x = sp.Symbol("x")
  
    fa = f.subs(x, a)
    fb = f.subs(x, b)
    
    if fa * fb >= 0:
        print("There is no sign change in the interval [a, b]. The bisection method cannot be applied.")
        return None
    
    xr = (a + b) / 2
    fxr = f.subs(x, xr)
    
    while abs(fxr) > tol:
        if fa * fxr < 0:
            b = xr
        elif fa * fxr > 0:
            a = xr
            fa = f.subs(x, a)
        
        xr = (a + b) / 2
        fxr = f.subs(x, xr)
    
    return xr

"""
#Example:
x = sp.Symbol("x")
f = x**4 + 7*x**3 - 7
a = 0
b = 1
tol = 1e-2

raiz_aprox = metodo_biseccion(f, a, b, tol)

if raiz_aprox is not None:
    print("Raíz aproximada encontrada:", raiz_aprox)
    print("Valor de f en la raíz aproximada:", f.subs(x, raiz_aprox))
"""