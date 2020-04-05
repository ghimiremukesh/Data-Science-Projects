# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:30:14 2018

@author: cipher
"""
# Spirit Animal: ApricotZebra

# Date Edited: 11/08/2018 

# Challenge #5

# Sources Consulted: Class Wiki

import numpy as np
import matplotlib.pyplot as plt



file = open('ApricotZebra.csv', 'r')
data = file.read()
data = data.split('\n')


f = {}
corrilation = []
x_line = []
y_line  = []
yp   = []
corr = []
actual = {}
colors = ['orchid', 'green', 'orange', 'aqua', 'teal']




for index in range(len(data)):
    data[index] = data[index].split(',')
    
data.pop()

# Append frequencies and their time and intensities to the dictionary 
for index in range(len(data)):
    time = np.float32(data[index][0])
    freq = np.float32(data[index][1])
    amp  = np.float32(data[index][2])   
    if freq in f:
        f[freq][0].append(time)
        f[freq][1].append(amp)
    else:
        f[freq] = [[time],[amp],[]]
index = 0
for key in f:
    plt.scatter(f[key][0],f[key][1], c = colors[index])
    index += 1
    cor = np.corrcoef(f[key][0], f[key][1])
    f[key][2].append(cor[0][1])
    corr.append(f[key][2][0])


# To find correlated data, minimum and maximum since one of the data set is negatively correlated and one of them is positively correlated
    
min_corr = min(corr)
max_corr = max(corr)


# Add the actual data set for regression analysis
for key in f:
    if f[key][2][0] == max_corr or f[key][2][0] == min_corr:
        actual[key] = f[key]

# Find the linear regression of each of the data set
        
for key in actual:    
        x = actual[key][0]
        y = actual[key][1]
        corr = np.float32(actual[key][2])
        m = corr * np.std(y)/np.std(x)
        b = np.mean(y) - np.mean(x)*m
        x1 = range(0,len(x))
        for index in range(len(x1)):
            x_line.append(x1[index])
            y_line.append(m*x1[index] + b)
        
        plt.plot(x_line, y_line, c='red')        
        x_line = []
        y_line = []
        
# Polynomial regression using numpy's polyfit and polyval

for key in actual:
        x = actual[key][0]
        y = actual[key][1]
        model_params = np.polyfit(x, y, 2)
        xp = range(0, len(x))
        yp.append(np.polyval(model_params, xp)) 
                   
plt.plot(xp, yp[0],yp[1], c= 'blue')               
plt.xlabel("Time (in Milliseconds)")
plt.ylabel("Intensity")
plt.show()

