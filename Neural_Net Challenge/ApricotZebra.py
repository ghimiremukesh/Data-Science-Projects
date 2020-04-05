# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 23:42:29 2018

@author: cipher
"""

# Spirit Animal: ApricotZebra

# Date Edited: 11/28/2018 

# Challenge #6 : Final Challenge

# Sources Consulted: Class Wiki

        
import neuro
from random import shuffle

def generateGrid():
    return  [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ]

def flattenGrid(grid):
    result = []
    for row in grid:
        result = result + row
    
    return result

one = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 0.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]

none = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]

two = [
[1.0,1.0,1.0,1.0,1.0],
[1.0,0.0,1.0,1.0,1.0],
[1.0,1.0,1.0,1.0,1.0],
[1.0,1.0,1.0,0.0,1.0],
[1.0,1.0,1.0,1.0,1.0],
]

two_2 = [
[1.0,1.0,1.0,1.0,1.0],
[1.0,1.0,1.0,0.0,1.0],
[1.0,1.0,1.0,1.0,1.0],
[1.0,0.0,1.0,1.0,1.0],
[1.0,1.0,1.0,1.0,1.0],
]

three = [
[1.0,1.0,1.0,1.0,1.0],
[1.0,0.0,1.0,1.0,1.0],
[1.0,1.0,0.0,1.0,1.0],
[1.0,1.0,1.0,0.0,1.0],
[1.0,1.0,1.0,1.0,1.0]
]

three_3 = [
[1.0,1.0,1.0,1.0,1.0],
[1.0,1.0,1.0,0.0,1.0],
[1.0,1.0,0.0,1.0,1.0],
[1.0,0.0,1.0,1.0,1.0],
[1.0,1.0,1.0,1.0,1.0]
]
 

four = [ 
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 1.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 1.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0] 
]

five = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 1.0, 0.0, 1.0],
    [1.0, 1.0, 0.0, 1.0, 1.0],
    [1.0, 0.0, 1.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]

six = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 1.0, 0.0, 1.0],
    [1.0, 0.0, 1.0, 0.0, 1.0],
    [1.0, 0.0, 1.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]

six_6 = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]
    
    
def generateInput(number):
    resultArray = []
    for i in range(0,6):
        for j in range(0, 6):
            grid = generateGrid()
            grid[i][j:j+5] = number[0]
            grid[i+1][j:j+5] = number[1]
            grid[i+2][j:j+5] = number[2]
            grid[i+3][j:j+5] = number[3]
            grid[i+4][j:j+5] = number[4]
            resultArray.append(flattenGrid(grid))
    return resultArray


# All the inputs
input_orig =  generateInput(one) + generateInput(two) + generateInput(three) + generateInput(four) + generateInput(five) + generateInput(six) + generateInput(two_2) + generateInput(three_3) + generateInput(six_6)
 


# All the targets
target_orig = [[0.1]]*36 + [[0.2]]*36 + [[0.3]]*36 + [[0.4]]*36 + [[0.5]]*36 + [[0.6]]*36  + [[0.2]]*36 + [[0.3]]*36 + [[0.6]]*36
# Associate each input with target
input_target = list(zip(input_orig, target_orig))

# Randomize
shuffle(input_target)

# Unpack into input and target
input, target = list(zip(*input_target))

network = []
reps = 1500
network = neuro.setup_network(input_orig)


neuro.train(network, input, target, reps)
neuro.writeNetworkToFile('Network.net', network)

test_input = [1,1,1,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

test_input_list = []

for items in test_input:
    test_input_list.append(float(items))
    
pred = neuro.predict(network, test_input_list)
   

print(pred)



