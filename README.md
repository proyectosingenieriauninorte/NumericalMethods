# Numerical Methods Repository

This repository contains implementations of numerical methods in Python. The included methods are useful for solving mathematical problems using computational techniques. They are used to build the **marlonpy** Python package, which aims to help Systems Engineering students at Universidad del Norte, especially in their Computational Solutions to Engineering Problems course.

Check out the oficial package site: https://pypi.org/project/marlonpy/0.1.1/

## Team: NRC 2381
- Lena Carolina Castillo De la Espriella
- Gabriela De Jesús Bula Pavia
- Edgar Andrés Garcia Davila

## Table of Contents

- [Repository Contents](#repository-contents)
- [Repository Structure](#repository-structure)
- [Dependencies](#dependencies)
- [Installation and Usage](#installation-and-usage)
- [License](#license)

## Repository Contents

This repository currently includes implementations of the following methods:
- **Number Conversions**: Binary to Decimal, IEEE 754.
- **Root-Finding Methods**: Includes Bisection, Fixed Point, Newton-Raphson, Regula Falsi, and Secant methods.
- **Linear Regression**: Techniques for modeling relationships between variables.
- **Numerical Differentiation**: Methods for approximating derivatives.
- **Numerical Integration**: Techniques such as the Trapezoidal Rule, Gauss-Legendre, and Simpson's rule.
- **Differential Equation Solvers**: Includes methods like Runge-Kutta.
  
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

Each directory contains specific implementations of the mentioned methods.

## Dependencies

- [NumPy](https://www.numpy.org): the fundamental package for scientific computing in Python.
- [SymPy](https://www.sympy.org/en/index.html): a Python library for symbolic mathematics.
- [tabulate](https://pypi.org/project/tabulate/): Pretty-print tabular data in Python.

## Installation and Usage

Latest version of `Python 3.12.3`
```bash
pip install marlonpy==0.1.1
```

If the command `pip` does not work in your computer, please try: 
```bash
py -m pip install marlonpy==0.1.1
```

Now, you can use the library.
```bash
import marlonpy as mp
```

## License

This repository is licensed under the [MIT License](LICENSE).

