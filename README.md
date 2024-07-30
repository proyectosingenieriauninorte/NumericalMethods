# Numerical Methods Repository MarlonPy

Check out the oficial package site: https://pypi.org/project/marlonpy/

Package developed for Universidad del Norte, focused on the Engineering Division. Supervised by professors Augusto Salazar and Marlon Piñeres.

## Table of Contents

- [Numerical Methods Repository MarlonPy](#numerical-methods-repository-marlonpy)
  - [Table of Contents](#table-of-contents)
  - [Summary and Justification](#summary-and-justification)
  - [Repository Contents](#repository-contents)
  - [Repository Structure](#repository-structure)
  - [Dependencies](#dependencies)
  - [Installation and Usage Instructions](#installation-and-usage-instructions)
    - [Examples](#examples)
  - [Authors](#authors)
  - [License](#license)

## Summary and Justification
This repository contains implementations of numerical methods in Python. The included methods are useful for solving mathematical problems using computational techniques. They are used to build the **marlonpy** Python package, which aims to help Systems Engineering students at Universidad del Norte, especially in their Computational Solutions to Engineering Problems course.

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

## Installation and Usage Instructions

Latest version of `Python 3.12.3`
```bash
pip install marlonpy
```

If the command `pip` does not work in your computer, please try: 
```bash
py -m pip install marlonpy
```

Now, you can use the library.
```bash
import marlonpy as mp
```

### Examples
- IEEE 754 Conversion:
```
>>> from marlonpy.Conversions import ConversionIeee
>>> num = '01000010101010100100000000000000'
>>> print('El equivalente de num en decimal es', ConversionIeee.ieee754(num))
El equivalente de num en decimal es 85.125
```
- Regula Falsi:
```
>>> from marlonpy.Roots import RegulaFalsi
>>> import sympy as sp
>>> x = sp.Symbol('x')
>>> f = sp.sec(sp.exp(sp.sqrt(x + 1))) - 3
>>> a = 3
>>> b = 3.1
>>> print('La raíz aproximada es', RegulaFalsi.regula_falsi(f, a, b))
La raíz aproximada es 3.06741643635292
```
## Authors
- Lena Carolina Castillo De la Espriella: `LCCastillo03`
- Gabriela De Jesús Bula Pavia: `paviag`
- Edgar Andrés Garcia Davila: `EdgarGXI`

## Contributing

Thanks for your interest in contributing to this project.
Get started with our [Contributing Guide][contrib].

## License

This repository is licensed under the [MIT License](LICENSE).

[contrib]: https://github.com/proyectosingenieriauninorte/.github/blob/master/CONTRIBUTING.md

