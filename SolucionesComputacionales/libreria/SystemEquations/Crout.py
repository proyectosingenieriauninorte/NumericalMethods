import numpy as np

def crout_method(A, sol):
    """
    Performs LU decomposition (Crout) of a square matrix A and solves a linear system Ax = sol.
    
    Args:
        A (numpy.ndarray): Coefficient matrix of the linear system.
        sol (numpy.ndarray): Vector of constants in the linear system.
        
    Returns:
        numpy.ndarray: Solution vector containing the values of x, y, z (or more variables)
                       that satisfy the linear system Ax = sol.
    """
    # Extract coefficients from matrix A
    a = A[0][0]
    b = A[1][0]
    d = A[2][0]
    g = A[0][1] / a
    h = A[0][2] / a
    c = A[1][1] - b * g
    e = A[2][1] - d * g
    i = (A[1][2] - b * h) / c
    f = A[2][2] - d * h - e * i
    
    # Construct lower triangular matrix L and upper triangular matrix U
    L = np.array([[a, 0, 0], [b, c, 0], [d, e, f]])
    U = np.array([[1, g, h], [0, 1, i], [0, 0, 1]])
    
    # Solve Ly = sol
    y = np.linalg.solve(L, sol)
    
    # Solve Ux = y
    x = np.linalg.solve(U, y)
    
    print(f"x: {x[0]:.4f}")
    print(f"y: {x[1]:.4f}")
    print(f"z: {x[2]:.4f}")

    return x

"""
#Example:
A = np.array([[27, 6, -1], [6, 15, -2], [1, 1, 54]])
sol = np.array([85, 72, 110])

result = crout_method(A, sol)
"""