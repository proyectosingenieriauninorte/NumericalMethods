import sympy as sp

def taylor(f, a, n, equis):
    """
Compute the Taylor series approximation of a function f centered at a, up to the nth term,
evaluated at the point equis.

    Args:
        f (sympy.core.expr.Expr): The function to approximate.
        a (float): The center point for the Taylor series.
        n (int): The highest degree of the Taylor series approximation.
        equis (float): The point at which to evaluate the Taylor series approximation.

    Returns:
        tuple: A tuple containing:
            - float: The theoretical value of f(equis) using the original function.
            - float: The experimental value of f(equis) using the Taylor series approximation.
            - float: The relative error (in percentage) between the theoretical and experimental values.
            - float: The absolute error between the theoretical and experimental values.
            - sympy.core.expr.Expr: The Taylor series approximation up to the nth term.
    """

    x = sp.Symbol("x")
    suma = 0
    
    for i in range(n + 1):
        suma += (sp.diff(f, x, i).subs(x, a) * (x - a)**i) / sp.factorial(i)
    
    valor_teorico = f.subs(x, equis).evalf()
    valor_experimental = suma.subs(x, equis).evalf()
    
    error_rel = abs((valor_teorico - valor_experimental) / valor_teorico) * 100
    error_ab = abs(valor_teorico - valor_experimental)
    
    return valor_teorico, valor_experimental, error_rel, error_ab, suma

"""
Example:

x = sp.Symbol("x")
f = sp.cos(3*x) + sp.sin(3*x) + sp.exp(x)
a = 0
n = 10
equis = 1

theoretical_value, experimental_value, rel_error, ab_error, sum = taylor(f, a, n, equis)

print(theoretical_value, experimental_value, rel_error, ab_error, sum)

"""