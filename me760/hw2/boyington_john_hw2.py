import numpy as np







# --------------------------------------------------problem 2
A = np.array([[1,  1, -1],
              [0,  8,  6],
              [-2, 4,  6]])

b = np.array([9, -6, 40])

sol2a = np.linalg.solve(A, b)
print(sol2a)
print(np.allclose(np.dot(A, sol2a), b))