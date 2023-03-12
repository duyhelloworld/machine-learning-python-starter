import numpy as np

# print("Hello World, np = " + str(np.ALLOW_THREADS))

# Matrix
_A = [ [1, 4, 7], [2, 5, 8], [10, 22, 34]]
A = np.array(object=_A, dtype=int, ndmin=2) 

# Vector
_B = [1, 4, 8, 9, 100]
# print(_B)

# print("0, 0    ", A[0, 0])
# print(":, 2    ", A[:, 2])
# print("2, :    ", A[2, :])

# print("A = \n", A)
_B = [1, 2, 4]
# print("_B = ", _B)
# print(A.dot(_B))
# print(_B * A)
# print(A@_B)

_C = [[2, 2], [5, 5], [8, 8]]
C = np.array(_C)
# print(C.dot(A))
# print(A.dot(C))

# print(np.eye(3))

# A T
_A_t = [[1, 0, 1], [0, 1, 0], [1, 1, 1]]
# space = np.linspace(2.0, 10.0, num=10)

A_inver = np.around(np.linalg.pinv(_A_t))
# print(A_inver)
"""
0   0   0
0   1   0
0   0   0
"""

A_transpose = np.transpose(_A_t)
print(A_transpose)

A_size = np.size(_A_t)
A_size_row = np.size(_A_t, 0)
A_size_col = np.size(_A_t, 1)
# sum, max, min
