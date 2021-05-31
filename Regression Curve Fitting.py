from pandas import read_csv
import numpy as np
from matplotlib import pyplot
from scipy.optimize import curve_fit
url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/longley.csv'
dataframe= read_csv(url,header=None)
data=dataframe.values
xdata,ydata=data[:,4],data[:,-1]

def objective(x, a, b, c, d, e, f, g, k):
	return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + (f * x**6) + (g * x**7) + k

def objective2(x, a, k):
	return (a * x) + k

def objective3(x, a,b,c,k):
	return (a * x) + (b * x**2) + (c * x**3) +  k

def objective4(x, a,b,c,d,e,k):
	return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + k


popt,_ =curve_fit(objective,xdata,ydata,method='dogbox')

popt2,_ =curve_fit(objective2,xdata,ydata,method='dogbox')

popt3,_ =curve_fit(objective3,xdata,ydata,method='dogbox')

popt4,_ =curve_fit(objective4,xdata,ydata,method='dogbox')

pyplot.subplot(2,2,1)
pyplot.scatter(xdata, ydata)
x_line = np.arange(min(xdata), max(xdata), 1)
y_line = objective(x_line, *popt)
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.title('7th order polynomial linear regression')
pyplot.xlabel("Population size ")
pyplot.ylabel("Employed people ")


pyplot.subplot(2,2,2)
pyplot.scatter(xdata, ydata)
x_line3 = np.arange(min(xdata), max(xdata), 1)
y_line3 = objective4(x_line3, *popt4)
pyplot.plot(x_line3, y_line3, '--', color='red')
pyplot.title('5th order polynomial linear regression')
pyplot.xlabel("Population size ")
pyplot.ylabel("Employed people ")


pyplot.subplot(2,2,3)
pyplot.scatter(xdata, ydata)
x_line2 = np.arange(min(xdata), max(xdata), 1)
y_line2 = objective3(x_line2, *popt3)
pyplot.plot(x_line2, y_line2, '--', color='red')
pyplot.title('3rd order polynomial linear regression')
pyplot.xlabel("Population size ")
pyplot.ylabel("Employed people ")


pyplot.subplot(2,2,4)
pyplot.scatter(xdata, ydata)
x_line1 = np.arange(min(xdata), max(xdata), 1)
y_line1 = objective2(x_line1, *popt2)
pyplot.plot(x_line1, y_line1, '--', color='red')
pyplot.title('1st order polynomial linear regression')
pyplot.xlabel("Population size ")
pyplot.ylabel("Employed people ")
pyplot.show()