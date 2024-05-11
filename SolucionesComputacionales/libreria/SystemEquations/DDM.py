def DDM(m, n) :
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