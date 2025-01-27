import numpy as np

#  first task
a = np.array ([[1, 1, 1], [1, 1.4, 0], [1, 0, 1.2]])
b = np.matrix ("50000; 45000; 28000")

a_lin = np.linalg.solve(a,b)

x = a_lin[0]
y = a_lin[1]
z = a_lin[2]

print("Перший банк (x):", x)
print("Другий банк (y):", y)
print("Третій банк (z):", z)

#  second task
a = np.matrix ("1, 1, 1; -1, 1, 0; 1, 0, -1")
b = np.matrix ("1328; 120; 100")

a_lin = np.linalg.solve(a,b)

x = a_lin[0]
y = a_lin[1]
z = a_lin[2]

print("IPhone 12:", x, "IPhone 13:", y, "IPhone 15:", z)
#  print("IPhone 13:", y)
#  print("IPhone 15:", z)


# third task

a = np.array([[3, 0, 3], [6, 1/4, 0], [1, 1/3, 1]])
b = np.array([1, 1, 1])

a_lin = np.linalg.solve(a, b)

a2 = 1 / a_lin[0]
b2 = 1 / a_lin[1]
c2 = 1 / a_lin[2]

print(a2, b2, c2)

# fourth task

a = np.matrix ("1, 1, 1; 9, 3, 1; 1, -1, 1")
b = np.matrix ("12; 54; 2")

a_lin = np.linalg.solve(a,b)

x = a_lin[0]
y = a_lin[1]
z = a_lin[2]

print(x, y, z)
