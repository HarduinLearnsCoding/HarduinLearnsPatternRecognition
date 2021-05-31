from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#optimizing fn generation

def gauss(x, K, B, x0, stddev):
    return K + B * np.exp(-(x - x0) ** 2 / (2 * stddev ** 2))

def gaussian_curve_fit(x, y):
    mean = sum(x * y) / sum(y)
    stddev = np.sqrt(sum(y * (x - mean) ** 2) / sum(y))
    popt, pcov = curve_fit(gauss, x, y, p0=[min(y), max(y), mean, stddev])
    return popt

#data creation

np.random.seed(104)  
xdata = np.linspace(3, 10, 100)

#Perfect gaussian 

ydata_perfect = gauss(xdata, 20, 5, 6, 1)
ydata = np.random.normal(ydata_perfect, 1, 100)

K, B, x0, stddev = gaussian_curve_fit(xdata, ydata)


plt.plot(xdata, ydata, 'c', label='Noisy Data')
plt.plot(xdata, ydata_perfect, '-.k', label='Perfect Data')
plt.plot(xdata, gauss(xdata, *gaussian_curve_fit(xdata, ydata)), ':r', label='fit')
plt.legend()
plt.title('Gaussian fit')
plt.xlabel('X Data')
plt.ylabel('Y Data')
plt.show()