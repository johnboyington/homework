import numpy as np


# --------------------------------------------------problem 1
print('\nProblem 1 \n')

C = np.array([[4,  6,  2],
              [6,  0,  3],
              [2,  3, -1]])

print(C.dot(C))


# --------------------------------------------------problem 2
print('\nProblem 2 \n')

A = np.array([[1,  1, -1],
              [0,  8,  6],
              [-2, 4,  -6]])

b = np.array([9, -6, 40])

sol2a = np.linalg.solve(A, b)
print('Solution =', sol2a)
print('Det = ', np.linalg.det(A))
print('Inverse = \n', np.linalg.inv(A))
