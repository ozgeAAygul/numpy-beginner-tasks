import numpy as np
# 1D Array
array_1 = np.array([1, 2, 3, 4, 5])
# 2D Array
array_2 = np.array([[1, 2, 3], [4, 5, 6]])

# Get Shape
print(f"Shape of array1: {array_1.shape}")
print(f"Shape of array2: {array_2.shape}")

# Get Dimension
print(f"\nNumber of dimension (array1): {array_1.ndim}")
print(f"Number of dimension (array2): {array_2.ndim}")

# Get Type
print(f"\nType of array1: {array_1.dtype}")
print(f"Type of array2: {array_2.dtype}")

arr1_float = array_1.astype(float)
print(f"\nFloat version of array1: \n{arr1_float}\ntype of arrayy1: {arr1_float.dtype}\n")

arr2_float = array_2.astype(float)
print(f"Float version of array2: \n{arr2_float}\ntype of arrayy2: {arr2_float.dtype}")
