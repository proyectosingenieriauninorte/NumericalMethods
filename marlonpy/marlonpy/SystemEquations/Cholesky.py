import numpy as np
from fractions import Fraction

class Cholesky:
    """
Performs Cholesky decomposition of a symmetric, positive definite matrix A and solves a linear system Ax = sol.

Args:
    A (numpy.ndarray): Coefficient matrix of the linear system.
    sol (numpy.ndarray): Vector of constants in the linear system.

Attributes:
    L (numpy.ndarray): Lower triangular matrix obtained from Cholesky decomposition.
    x (numpy.ndarray): Solution vector containing the values of the variables that satisfy Ax = sol.
    y (numpy.ndarray): Intermediate solution vector for the system Ly = sol.

Returns:
    str: A formatted string representing the solution vector x with both decimal values and their fractional equivalents.
         Example: "Thus, x = 28.5833 = 343/12, y = -7.6667 = -23/3, z = 1.3333 = 4/3".
"""

    def __init__(self, A, sol):
        self.A = A  # Coefficient matrix
        self.sol = sol  # Solution vector
        self.n = A.shape[0]  # Matrix size
        self.L = np.zeros((self.n, self.n))  # Lower triangular matrix
        self.y = np.zeros(self.n)  # Intermediate vector y
        self.x = np.zeros(self.n)  # Solution vector x

    def is_symmetric(self):
        return np.allclose(self.A, self.transpose(self.A))

    def transpose(self, matrix):
        return matrix.T

    def det(self, submatrix):
        submatrix = np.array(submatrix)  # Ensure it's a NumPy array
        if submatrix.shape == (1, 1):  # Handle single-element matrices
            D = submatrix[0, 0]
        elif submatrix.shape == (2, 2):  # Handle 2x2 matrices
            D = submatrix[0, 0] * submatrix[1, 1] - submatrix[0, 1] * submatrix[1, 0]
        elif submatrix.shape == (3, 3):  # Handle 3x3 matrices
            D = (
                submatrix[0, 0] * submatrix[1, 1] * submatrix[2, 2]
                + submatrix[1, 0] * submatrix[2, 1] * submatrix[0, 2]
                + submatrix[2, 0] * submatrix[0, 1] * submatrix[1, 2]
                - submatrix[0, 2] * submatrix[1, 1] * submatrix[2, 0]
                - submatrix[1, 2] * submatrix[2, 1] * submatrix[0, 0]
                - submatrix[2, 2] * submatrix[0, 1] * submatrix[1, 0]
            )
        else:  # For larger matrices
            D = 0
            size = len(submatrix)
            for i in range(size):
                for j in range(size):
                    sign = (-1) ** j
                    sub = [
                        [submatrix[row][col] for col in range(size) if col != j]
                        for row in range(size) if row != i
                    ]
                    sub = np.array(sub)  # Ensure submatrix is a NumPy array
                    D += sign * submatrix[0][j] * self.det(sub)
        return D

    def is_positive_definite(self):
        for k in range(1, self.n + 1):
            submatrix = self.A[:k, :k]
            D = self.det(submatrix)
            if D <= 0:
                return False

        return True

    def decompose(self):
        print("\033[1mMatrix A:\033[0m")
        print(self.A)
        print()
        if self.is_symmetric():
            if self.is_positive_definite():
                print("\033[1mThe matrix is symmetric and positive definite.\033[0m\n")
            else:
                print("\033[1mThe matrix is symmetric but not positive definite.\033[0m\n")
        else:
            if self.is_positive_definite():
                print("\033[1mThe matrix is not symmetric but it is positive definite.\033[0m\n")
            else:
                print("\033[1mThe matrix is neither symmetric nor positive definite.\033[0m\n")

        if self.is_symmetric():
            if self.is_positive_definite():
                # Step 2: Calculate L
                for i in range(self.n):
                    for j in range(i + 1):
                        sum_val = self.A[i, j]
                        for k in range(j):
                            sum_val -= self.L[i, k] * self.L[j, k]
                        if i == j:
                            self.L[i, j] = np.sqrt(sum_val)
                        else:
                            self.L[i, j] = sum_val / self.L[j, j]
                    print(f"\033[1mIteration {i + 1}:\033[0m")
                    print("Matrix L (Lower Triangular):")
                    print(self.L)
                    print()

                # Step 2.1: Solve Ly = b
                for i in range(self.n):
                    self.y[i] = (self.sol[i] - np.dot(self.L[i, :i], self.y[:i])) / self.L[i, i]
                print("\033[1my = \033[0m", self.y, "\n")

                # Step 3: Calculate U
                U = self.transpose(self.L)

                # Print upper triangular matrix U
                print("Matrix U (Upper Triangular):")
                print(U, "\n")

                # Step 3.1: Solve Ux = y
                for i in range(self.n - 1, -1, -1):
                    self.x[i] = (self.y[i] - np.dot(self.L[i + 1:self.n, i], self.x[i + 1:self.n])) / self.L[i, i]

                # Show the solutions x
                print("\033[1mx = \033[0m", self.x)

                self.show_results()

    def show_results(self):
        sol_x = float(self.x[0].item())
        sol_y = float(self.x[1].item())
        sol_z = float(self.x[2].item())

        # Convert solutions to fractions
        frac_x = Fraction(sol_x).limit_denominator()
        frac_y = Fraction(sol_y).limit_denominator()
        frac_z = Fraction(sol_z).limit_denominator()

        print(f"\n\033[1mThus, x = {self.x[0]:.4f} = {frac_x}, y = {self.x[1]:.4f} = {frac_y}, z = {self.x[2]:.4f} = {frac_z}\033[0m")

""""
A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
sol = np.array([1, 2, 3, 4])

cholesky = Cholesky(A, sol)
cholesky.decompose()
"""