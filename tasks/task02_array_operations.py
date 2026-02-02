import numpy as np

# 1D Array operations
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a + 5)
print(b * 2)

# 2D Array Operations
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix * 2)
print(matrix + 10)

# NumPy Functions Operations
print(np.sum(matrix))
print(np.mean(matrix)) 
print(np.mean(matrix, axis=0))
print(np.mean(matrix, axis=1))
print(np.max(a))
print(np.min(b))