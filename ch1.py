import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

x_data = [1, 2, 3, 4, 5]
y_data = [3, 9, 27, 48, 54]
x_err = 0.5
y_err = [1, 2, 3, 4, 5]

plt.errorbar(x_data, y_data, xerr=x_err, yerr=y_err, fmt='o')

def func(x, a, b):
    return a*x + b


popt, pcov = curve_fit(func, x_data, y_data)
x_range = np.linspace(np.amin(x_data), np.amax(x_data), 100)
plt.plot(x_range, func(x_range, *popt))


plt.title("Example of a graph title")
plt.xlabel("An x-axis label")
plt.ylabel("A y-axis label using $LaTeX$ syntax")
plt.savefig("ch4.png")
plt.show()
