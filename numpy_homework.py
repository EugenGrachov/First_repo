import numpy as np

a = np.array ([[1, 1, 1], [1, 1.4, 0], [1, 0, 1.2]])
b = np.matrix ("50000; 45000; 28000")

a_lin = np.linalg.solve(a,b)

x = a_lin[0]
y = a_lin[1]
z = a_lin[2]

print("Перший банк (x):", x)
print("Другий банк (y):", y)
print("Третій банк (z):", z)


