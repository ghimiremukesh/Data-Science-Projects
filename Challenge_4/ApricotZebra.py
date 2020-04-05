# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:26:49 2018

@author: cipher
"""

# Spirit Name: ApricotZebra

# Date Edited: 10/30/2018

# Challenge #4

# Sources: Class wiki


import numpy as np
import matplotlib.pyplot as plt
import math


k_v = int(input('Enter k-value: '))

x_axis=[]
y_axis = []
change = []
map_x = []
map_y=[]
distance = {}


xx_axis=[]
yy_axis=[]
change_n=[]
value=[]


# function to calculate distance

def distcalc(a,b):
    return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))




file = open('data.csv', 'r')
data = file.read()
data = data.split('\n')


usmapf = open('us_outline.csv', 'r')
usmap = usmapf.read()
usmap = usmap.split('\n')


for index in range(len(usmap)):
    usmap[index] = usmap[index].split(',')

usmap = np.float32(usmap)
for index in range(len(usmap)):
    map_x.append(usmap[index][0])
    map_y.append(usmap[index][1])

for index in range(len(data)):
    data[index] = data[index].split(',')

data = np.float32(data)
for index in range(len(data)):
    x_axis.append(data[index][0])
    y_axis.append(data[index][1])
    change.append(data[index][2])
    
for row in range(0,195):
    for col in range(0,121):
        for j in range(len(data)):
            a = [row,col]
            dist = distcalc(data[j],a)
            distance[dist] = data[j][2]    
        xx_axis.append(row)
        yy_axis.append(col)
        cs = 0
        for key in sorted(distance):
            value.append(distance[key])
        
        for index in range(k_v):
            cs = cs + value[index]
        cs= cs/k_v
        change_n.append(cs)
        distance={}
        value = []



        
        

plt.scatter(x_axis, y_axis, c=change, cmap='viridis')
plt.scatter(xx_axis,yy_axis, c=change_n, cmap = 'viridis')
plt.plot(map_x, map_y, c='black')
plt.show()