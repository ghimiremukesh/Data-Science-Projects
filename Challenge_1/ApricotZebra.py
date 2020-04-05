# -*- coding: utf-8 -*-

# Written in Python3

# Spirit Animal: ApricotZebra

# Date Edited: 09/14/2018 

# Challenge #1

# source: https://stackoverflow.com/questions/14827650/pyplot-scatter-plot-marker-size  //used for marker size (s)



import numpy as np
import matplotlib.pyplot as plt

file = open("ApricotZebra_ch1.csv", "r")
data = file.read()
data = data.replace(" ", "") #found a space before frequency entries; just to be sure
data = data.split("\n")   #split by lines

x_axis = []  #for the scatter plot
y_axis = []

x_axis_avg = []  #for average data to plot the line
y_axis_avg = []

#for title
fq = 0;

#split data by comma

for index in range(0, len(data)):
    data[index] = data[index].split(",")

# to remove a blank entry at the end of data
data.pop()

# set x and y axis
for index in range(0, len(data)):
    data[index] = np.float32(data[index])
    if (data[index][2] > 70):
        fq = data[index][2]
        x_axis.append(data[index][0])
        y_axis.append(data[index][1]) 
    

sum = y_axis[0]
counter = 1
avg = 0

# for mean value of the frequency

for i in range(0, len(y_axis)-1):
    if x_axis[i] == x_axis[i+1]:
        sum += y_axis[i+1] 
        counter += 1
        
        # since the last sets of data are for 70, this block calculates average for them.
        if i == len(y_axis)-2:
            counter += 1
            avg = sum/counter
            x_axis_avg.append(x_axis[i])
            y_axis_avg.append(avg)
         
    else:
        avg = sum/counter
        x_axis_avg.append(x_axis[i])
        y_axis_avg.append(avg)
        avg = 0
        sum = y_axis[i+1] 
        counter = 1


plt.scatter(x_axis, y_axis, s=15)
plt.plot(x_axis_avg, y_axis_avg, c="red", linewidth = 4.0)
plt.xlabel("Time (in Milliseconds)")
plt.ylabel("Amplitude")
plt.title("Amplitude vs Time for "+ str(fq) + " Hz Radio Station")
plt.show()


            
        




    
    
        
        
        
        


    

        
    