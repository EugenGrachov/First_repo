import numpy as np

a = np.eye(4, k=-1, dtype=float)
print (a)

a1 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print (a1)

a2 = np.diag(a1)
print(a2)

b = np.diag(a2)
print(b)

b1 = a1.T
print(b1)

a3 = np.matrix("1, 2, 3; 4, 5, 6")
b2 = a3.reshape((3, 2))
print(b2)

