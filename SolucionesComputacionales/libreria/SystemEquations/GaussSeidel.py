from sympy import *
import sympy as sp
from tabulate import tabulate

def gauss_seidel(fx, fy, fz, x0, y0, z0, tol):
    """
    Solves a system of equations using the Gauss Seidel iterative method.

    Args:
        fx (sympy expression): The equation representing x in terms of y and z.
        fy (sympy expression): The equation representing y in terms of x and z.
        fz (sympy expression): The equation representing z in terms of x and y.
        x0 (float): Initial guess for x.
        y0 (float): Initial guess for y.
        z0 (float): Initial guess for z.
        tol (float): Tolerance level for convergence.
    Prints:
        Table showing iteration details and final values of x, y, z.
    
    CAUTION: Make sure the matrix is DIAGONALLY DOMINANT
    """
    x, y, z = sp.symbols('x y z')
    n = 0
    x0_ant, y0_ant, z0_ant = 999, 999, 999
    Eax=Abs(x0-x0_ant)
    Eay=Abs(y0-y0_ant)
    Eaz=Abs(z0-z0_ant)
    Di = max([Eax,Eay,Eaz])
    d = [ [n, x0, y0,z0,Eax,Eay,Eaz,Di]]
  
    while(Di>tol):
      x0_ant=x0
      y0_ant=y0
      z0_ant=z0
      x0=(fx.subs(y,y0)).subs(z,z0).evalf()
      y0=(fy.subs(x,x0)).subs(z,z0).evalf()
      z0=(fz.subs(x,x0)).subs(y,y0).evalf()
      Eax=Abs(x0-x0_ant)
      Eay=Abs(y0-y0_ant)
      Eaz=Abs(z0-z0_ant)
      Di = max([Eax,Eay,Eaz])
      n=n+1
      d.append([n, "%.4f"%x0, "%.4f"%y0,"%.4f"%z0,"%.4f"%Eax,"%.4f"%Eay,"%.4f"%Eaz,"%.4f"%Di])

    headers = ["Iteración", "x", "y", "z", "|Eax|", "|Eay|", "|Eaz|", "Di"]
    print(tabulate(d, headers=headers, floatfmt=".4f"))
    print(f"x: {x0}")
    print(f"y: {y0}")
    print(f"z: {z0}")

"""
#Example
x, y, z = sp.symbols('x y z')
fx = (29 - 2*y - 3*z) / 10
fy = (7 - x-8*z) / 12
fz = (-3*x -5* y) / 9
x0 = 0
y0 = 0
z0 = 0
tol = 10**-1

gauss_seidel(fx, fy, fz, x0, y0, z0, tol)
"""
