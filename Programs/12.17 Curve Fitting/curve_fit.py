import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def f(x, a1, a2, t1, t2):
    return a1*np.exp(-x/t1) + a2*np.exp(-x/t2)
    
X, Y = np.loadtxt('some_data.dat', unpack=True)
par, cov = curve_fit(f, X, Y, p0=[1, 1, 1, 1])
R2 = 1 - np.sum((Y - f(X, *par))**2) / np.sum((Y - np.mean(Y))**2)
print('{:.4f}'.format(R2))

x, y = np.loadtxt('some_data.dat', unpack=True)
plt.xlabel('x (column1)')
plt.ylabel('y (column2)')
plt.plot(x, y, 'ko', label='some_data.dat')
plt.legend()
plt.show()
plt.savefig('my_plot.pdf')
