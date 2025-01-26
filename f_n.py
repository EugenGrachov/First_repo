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

a = np.matrix("1,2,3;4,5,6")
b = a.reshape((3, 2))
print(b)

a = np.matrix([[1, 2, 3], [4, 5, 6]])
b = a.flatten()
print(b)

a5 = np.matrix("1,2,3;0,1,2")
b5 = np.matrix("1,2;0,4;-1,0")
c5 = a5.dot(b5)
print(c5)

a22 = np.matrix("1,0,3;-1,-1,2;4,7,2")
det = round(np.linalg.det(a22))
print(det)

a = np.matrix("1,0,3;-1,-1,2;4,7,2")
a_inv = np.linalg.inv(a)
print(a_inv)

a = np.matrix("1,0,3;-1,-1,2;4,7,2")
w, v = np.linalg.eig(a)
print(w)
print(v)

a = np.matrix("1,2,5;1,-1,3;3,-6,-1")
b = np.matrix("-9;2;25")
a_inv = np.linalg.inv(a)
x = a_inv.dot(b)
print(x)

a = np.matrix("1,2,5;1,-1,3;3,-6,-1")
b = np.matrix("-9;2;25")
a_det = round(np.linalg.det(a))
a_1 = np.matrix(a)
a_1[:, 0] = b
a_2 = np.matrix(a)
a_2[:, 1] = b
a_3 = np.matrix(a)
a_3[:, 2] = b
x = [
    round(np.linalg.det(a_1)) / a_det,
    round(np.linalg.det(a_2)) / a_det,
    round(np.linalg.det(a_3)) / a_det,
]
print(x)

a = np.matrix([[1, 2, 5], [1, -1, 3], [3, -6, -1]])
b = np.matrix([[-9],[2], [25]])
a_inv = np.linalg.inv(a)
x = a_inv.dot(b)
print(x)

a_det = round(np.linalg.det(a))
a_1 = np.matrix(a)
a_1[:, 0] = b
a_2 = np.matrix(a)
a_2[:, 1] = b
a_3 = np.matrix(a)
a_3[:, 2] = b

x = [
    round(np.linalg.det(a_1)) / a_det,
    round(np.linalg.det(a_2)) / a_det,
    round(np.linalg.det(a_3)) / a_det,
]
print("a", x)

a = np.matrix("1,2,5;1,-1,3;3,-6,-1")
b = np.matrix("-9;2;25")
x = np.linalg.solve(a, b)
print(x)