import numpy as np

def linear_regression(equis, ye):
    """
    Performs linear regression analysis and returns the regression coefficients.

    Args:
        equis (numpy.ndarray): Array of x-values.
        ye (numpy.ndarray): Array of y-values.

    Returns:
        tuple: A tuple containing the regression coefficients (a0, a1).
    """
    sx = np.sum(equis)
    sy = np.sum(ye)
    sx2 = np.sum(equis**2)
    sxy = np.sum(equis * ye)
    n = len(equis)
    prox = np.mean(equis)
    proy = np.mean(ye)

    a1 = (n * sxy - sx * sy) / (n * sx2 - sx**2)
    a0 = proy - a1 * prox

    print(f"{'xi':<5} {'yi':<5} {'xi^2':<8} {'xi*yi':<8}")
    for xi, yi in zip(equis, ye):
        xi2 = xi**2
        xiyi = xi * yi
        print(f"{xi:<5} {yi:<5} {xi2:<8} {xiyi:<8}")

    print("___________________________")
    print(f"{sx:<5} {sy:<5} {sx2:<8} {sxy:<8}")

    print("Linear regression equation:")
    print(f"y = {a1} * x + {a0}")

    return a0, a1

"""
#Example:
equis = np.array([1, 2, 3, 4, 5, 6, 7])
ye = np.array([0.5, 2.5, 2, 4, 3.5, 6, 5.5])
a0, a1 = linear_regression(equis, ye)
"""