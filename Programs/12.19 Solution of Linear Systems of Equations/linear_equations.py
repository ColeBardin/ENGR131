import numpy as np

data = np.loadtxt(input())
A = data[:, :-1]
b = data[:, -1]
x = np.linalg.solve(A, b)
for n in x:
    print('{:.4f}'.format(n))
