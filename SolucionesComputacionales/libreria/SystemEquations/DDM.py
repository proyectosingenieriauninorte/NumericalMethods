def DDM(m, n) :
	"""
    Checks if a square matrix m is diagonally dominant by rows (DDF).

    Args:
        m (list of lists): The input matrix as a list of lists representing rows.
        n (int): The size of the square matrix (number of rows and columns).

    Returns:
        bool: True if the matrix is diagonally dominant by rows, False otherwise.
    """
	for i in range(0, n) :
		suma = 0
		for j in range(0, n) :
			suma = suma + abs(m[i][j])

		suma = suma - abs(m[i][i])

		if (abs(m[i][i]) < suma):
			return False
	return True

"""
#Example:
n = 3
m = ([[1/100, 2/100, 1/100], [2/100, 5/100,3/100], [3/100, 7/100, 1/100]])
if((DDM(m, n))):
	print("Sí")
else:
	print("No")
"""