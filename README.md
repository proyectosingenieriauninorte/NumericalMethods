# Numerical Methods Repository

This repository contains implementations of numerical methods focused on Python. The included methods are useful for solving mathematical problems using computational techniques.

## Team: NRC 2381
- Lena Carolina Castillo De la Espriella
- Gabriela De Jesús Bula Pavia
- Edgar Andrés Garcia Davila

## Repository Contents

This repository currently includes implementations of the following methods:
- **Number Conversions**: Binary to Decimal, IEEE 754.
- **Root-Finding Methods**: Includes Bisection, Fixed Point, Newton-Raphson, Regula Falsi, and Secant methods.
- **Linear Regression**: Techniques for modeling relationships between variables.
- **Numerical Differentiation**: Methods for approximating derivatives.
- **Numerical Integration**: Techniques such as the trapezoidal rule, Gauss-Legendre, and Simpson's rule.
- **Differential Equation Solvers**: Includes methods like Runge-Kutta.

More methods will be added over time as new implementations are developed.


## Repository Structure

The repository is structured as follows:

1. **Conversions**:
   - `/ConversionBinary.py`
   - `/ConversionIEEE754.py`
2. **Differential Equations:**
    - `/RungeKutta4th.py`
4. **Linear Regression**:
    - `/LinearRegression.py`
5. **Numerical Derivation**:
    - `/Derivative.py`
6. **Numerical Integration**:
    - `/GaussLegendre.py`
    - `/Simpson38.py`
    - `/TrapezoidalRule.py` 
4. **Roots**:
   - `/BisectionMethod.py`
   - `/FixedPoint.py`
   - `/NewtonRaphson.py`
   - `/RegulaFalsi.py`
   - `/SecantMethod.py`
5. **System Equations**:
   - `/Crout.py`
   - `/DDM.py`
   - `/Doolittle.py`
   - `/GaussSeidel.py`
   - `/Jacobi.py`

6. **Taylor Series**:
   - `/TaylorSeries.py`

Each directory contains specific implementations of the mentioned methods. As you develop more implementations or add new methods, you can expand this structure to maintain a clear and organized repository.


## Use of the library

 - Latest version of `Python 3.12.3`
```bash
pip install marlonpy
```
Now, you can use the library.
```bash
import marlonpy as mp
```

## License

This repository is licensed under the [MIT License](LICENSE).

