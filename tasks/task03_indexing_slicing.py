import numpy as np

# 1D Array
arr = np.array([10, 20, 30, 40, 50, 60])
# print the first index
print(arr[0])
# print the last index
print(arr[-1])
# print the middle indexes
print(arr[1:-1])
# print the last three indexes
print(arr[-3:]) 

# 2D Array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print index '5'
print(matrix[1, 1])
# print the first row
print(matrix[0, :])
# print the second column
print(matrix[:, 1])
# print the bottom right corner
print(matrix[-1,-1])
# print the first two row & the first two column
print(matrix[0:2, 0:2])
