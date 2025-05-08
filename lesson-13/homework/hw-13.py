# import numpy as np
# vector = np.arange(10, 50)
# print(vector) 

# import numpy as np
# matrix = np.arange(9).reshape(3, 3)
# print(matrix)

# import numpy as np
# identity_matrix = np.eye(3, dtype=int)
# print(identity_matrix)

# import numpy as np
# random_array = np.random.rand(3, 3, 3)
# print(random_array)

# import numpy as np
# random_array = np.random.rand(10, 10)
# min_value = random_array.min()
# max_value = random_array.max()
# print("Random 10x10 Array:")
# print(random_array)
# print("\nMinimum Value:", min_value)
# print("Maximum Value:", max_value)

# import numpy as np
# random_vector = np.random.rand(30)
# mean_value = random_vector.mean()
# print("Random Vector:", random_vector)
# print("Mean Value:", mean_value)

# import numpy as np
# matrix = np.random.rand(5, 5) * 10
# min_vals = matrix.min(axis=0)
# max_vals = matrix.max(axis=0)
# normalized_matrix_min_max = (matrix - min_vals) / (max_vals - min_vals)
# print("Original Matrix:")
# print(matrix)
# print("\nNormalized Matrix (Min-Max):")
# print(normalized_matrix_min_max)

# import numpy as np
# a = np.random.rand(5, 3)
# b = np.random.rand(3, 2)
# c = np.matmul(a, b)
# print("Matrix a (5x3):")
# print(a)
# print("\nMatrix b (3x2):")
# print(b)
# print("\nMatrix Product c (5x2):")
# print(c)

# import numpy as np
# a = np.random.rand(3, 3)
# b = np.random.rand(3, 3)
# c = np.dot(a, b)
# print("Matrix a:")
# print(a)
# print("\nMatrix b:")
# print(b)
# print("\nDot Product of a and b:")
# print(c)

# import numpy as np
# matrix = np.random.rand(4, 4)
# transposed_matrix = np.transpose(matrix)
# print("Original Matrix:")
# print(matrix)
# print("\nTransposed Matrix:")
# print(transposed_matrix)

# import numpy as np
# matrix = np.random.rand(3, 3)
# determinant = np.linalg.det(matrix)
# print("Matrix:")
# print(matrix)
# print("\nDeterminant:", determinant)

# import numpy as np
# a = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])
# b = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ])
# c = np.matmul(a, b)
# print("Matrix a (3x4):")
# print(a)
# print("\nMatrix b (4x3):")
# print(b)
# print("\nMatrix Product c (3x3):")
# print(c)

# import numpy as np
# x = np.random.rand(3, 3)
# y = np.random.rand(3)
# result = np.dot(x, y)
# print("Matrix x (3x3):")
# print(x)
# print("\nVector y (3x1):")
# print(y)
# print("\nMatrix-Vector Product:")
# print(result)

# import numpy as np
# a = np.array([
#     [3, -2, 5],
#     [1,  4, 0],
#     [2,  3, 1]
# ])
# b = np.array([7, 3, 4])
# x = np.linalg.solve(a, b)
# print("Solution vector x:")
# print(x)

# import numpy as np
# matrix = np.random.rand(5, 5)
# row_sums = np.sum(matrix, axis=1)
# col_sums = np.sum(matrix, axis=0)
# print("Matrix:")
# print(matrix)
# print("\nRow-wise sums:")
# print(row_sums)
# print("\nColumn-wise sums:")
# print(col_sums)
