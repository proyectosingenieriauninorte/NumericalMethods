import numpy as np

def doolittle(A, sol):
    """
    Performs LU decomposition (Doolittle) of a square matrix A and solves a linear system Ax = sol.
    
    Args:
        A (numpy.ndarray): Coefficient matrix of the linear system.
        sol (numpy.ndarray): Vector of constants in the linear system.
        
    Returns:
        numpy.ndarray: Solution vector containing the values of x, y, z (or more variables)
                       that satisfy the linear system Ax = sol.
    """
    #Extraction of the coefficients of matrix A    
    d = A[0][0]
    e = A[0][1]
    f = A[0][2]
    a = A[1][0] / d
    b = A[2][0] / d
    g = A[1][1] - a * e
    h = A[1][2] - a * f
    c = (A[2][1] - b * e) / g
    i = A[2][2] - b * f - c * h

    #L and U matrices
    L = np.array([[1, 0, 0], [a, 1, 0], [b, c, 1]])
    U = np.array([[d, e, f], [0, g, h], [0, 0, i]])

    #Solving Ly = sol
    y = np.linalg.solve(L, sol)

    #Solving Ux = y
    x = np.linalg.solve(U, y)

    print(f"x: {x[0]:.4f}")
    print(f"y: {x[1]:.4f}")
    print(f"z: {x[2]:.4f}")

    return x

"""
#Example:
A = np.array([[5, 1, 1], 
             [1, 3, 0], 
            [1, 1, 3]])
sol = np.array([10, 20, 30])

result = doolittle(A, sol)
"""

