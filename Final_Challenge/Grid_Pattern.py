# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 08:57:35 2018

@author: cipher
"""

from copy import deepcopy # to copy the list on a differnt memeory address 
import neuro


face =  list(range(10,0))

index = 0

parentlist = []
newlist = []

# A list representing 10 x 10 grid
for x in range(10):
    innerlist = []
    for y in range(10):
        innerlist.append(float(0))
    newlist.append(innerlist)

newlist_dice = deepcopy(newlist)


# Generating all possible 5 x 5 dice pattern in the grid
                 
start = True
x_start_index = 0
y_start_index = 0

while start == True:   
    for x in range(x_start_index, x_start_index + 5):
        for y in range(y_start_index, y_start_index + 5):
            newlist_dice[x][y] = float(1)
    parentlist.append(newlist_dice)
    newlist_dice = deepcopy(newlist)
    y_start_index += 1
    if (y_start_index + 4) > 9:
        x_start_index += 1
        y_start_index = 0
    if ((x_start_index + 4) > 9) or ((y_start_index + 4) > 9):
        start = False                   
    
                          
#for index in range(len(parentlist)):               
#   for sindex in range(len(parentlist[index])):
#       print(parentlist[index][sindex])
#   print() 

#print(len(parentlist))

# Functions to Generate all the possible grid patterns with all possible dice rolls         

def GenerateOne(dice):
    x_start_index = 0
    y_start_index = 0
    loop = True
    while loop:
        if dice[x_start_index][y_start_index] == 1:
            x_start_index += 2
            y_start_index += 2
            loop = False
        elif y_start_index < 9:
            y_start_index += 1
        elif y_start_index == 9:
            x_start_index += 1
            y_start_index = 0
    dice[x_start_index][y_start_index] = float(0)        
    return dice

def GenerateTwo(dice):
    x_start_index = 0
    y_start_index = 0
    loop = True
    while loop:
        if dice[x_start_index][y_start_index] == 1:
            dice[x_start_index + 1][y_start_index + 1] = float(0)
            dice[x_start_index + 3][y_start_index + 3] = float(0)
            loop = False
        elif y_start_index < 9:
            y_start_index += 1
        elif y_start_index == 9:
            x_start_index += 1
            y_start_index = 0       
    return dice

def GenerateThree(dice):
    x_start_index = 0
    y_start_index = 0
    loop = True
    while loop:
        if dice[x_start_index][y_start_index] == 1:
            dice[x_start_index + 1][y_start_index + 1] = float(0)
            dice[x_start_index + 2][y_start_index + 2] = float(0)
            dice[x_start_index + 3][y_start_index + 3] = float(0)
            loop = False
        elif y_start_index < 9:
            y_start_index += 1
        elif y_start_index == 9:
            x_start_index += 1
            y_start_index = 0       
    return dice

def GenerateFour(dice):
    x_start_index = 0
    y_start_index = 0
    loop = True
    while loop:
        if dice[x_start_index][y_start_index] == 1:
            dice[x_start_index + 1][y_start_index + 1] =float(0)
            dice[x_start_index + 1][y_start_index + 3] = float(0)
            dice[x_start_index + 3][y_start_index + 1] = float(0)
            dice[x_start_index + 3][y_start_index + 3] = float(0)
            loop = False
        elif y_start_index < 9:
            y_start_index += 1
        elif y_start_index == 9:
            x_start_index += 1
            y_start_index = 0       
    return dice

def GenerateFive(dice):
    x_start_index = 0
    y_start_index = 0
    loop = True
    while loop:
        if dice[x_start_index][y_start_index] == 1:
            dice[x_start_index + 1][y_start_index + 1] = float(0)
            dice[x_start_index + 1][y_start_index + 3] = float(0)
            dice[x_start_index + 2][y_start_index + 2] = float(0)
            dice[x_start_index + 3][y_start_index + 1] = float(0)
            dice[x_start_index + 3][y_start_index + 3] = float(0)
            loop = False
        elif y_start_index < 9:
            y_start_index += 1
        elif y_start_index == 9:
            x_start_index += 1
            y_start_index = 0       
    return dice

def GenerateSix(dice):
    x_start_index = 0
    y_start_index = 0
    loop = True
    while loop:
        if dice[x_start_index][y_start_index] == 1:
            dice[x_start_index + 1][y_start_index + 1] = float(0)
            dice[x_start_index + 1][y_start_index + 3] = float(0)
            dice[x_start_index + 2][y_start_index + 1] = float(0)
            dice[x_start_index + 2][y_start_index + 3] = float(0)
            dice[x_start_index + 3][y_start_index + 1] = float(0)
            dice[x_start_index + 3][y_start_index + 3] = float(0)
            loop = False
        elif y_start_index < 9:
            y_start_index += 1
        elif y_start_index == 9:
            x_start_index += 1
            y_start_index = 0       
    return dice

ones = deepcopy(parentlist)
twos = deepcopy(parentlist)
threes = deepcopy(parentlist)
fours = deepcopy(parentlist)
fives = deepcopy(parentlist)
sixes = deepcopy(parentlist)

ones_list = [] 
twos_list = []
threes_list = []
fours_list = []
fives_list = []
sixes_list = []

for index in range(len(ones)):
    onelist = GenerateOne(ones[index])
    ones_list.append(onelist)
    onelist = deepcopy(parentlist)
    twolist = GenerateTwo(twos[index])
    twos_list.append(twolist)
    twolist = deepcopy(parentlist)
    threelist = GenerateThree(threes[index])
    threes_list.append(threelist)
    threelist = deepcopy(parentlist)    
    fourlist = GenerateFour(fours[index])
    fours_list.append(fourlist)
    fourlist = deepcopy(parentlist) 
    fivelist = GenerateFive(fives[index])
    fives_list.append(fivelist)
    fivelist = deepcopy(parentlist)
    sixlist = GenerateSix(sixes[index])
    sixes_list.append(sixlist)
    sixlist = deepcopy(parentlist)

test_list = []

inputs = []
ones_test_inputs = []
twos_test_inputs = []
threes_test_inputs = []
fours_test_inputs = []
fives_test_inputs = []
sixes_test_inputs = []
targets = []

for index in range(len(ones_list)):
    for x in range(len(ones_list[index])):
        for y in range(len(ones_list[index][x])):
            test_list.append(ones_list[index][x][y])
#    ones_test_inputs.append(test_list)
    inputs.append(test_list)
    targets.append([float(0.1)])
    test_list = []

#inputs.append(ones_test_inputs)

for index in range(len(twos_list)):
    for x in range(len(twos_list[index])):
        for y in range(len(twos_list[index][x])):
            test_list.append(twos_list[index][x][y])
#    twos_test_inputs.append(test_list)
    inputs.append(test_list)
    targets.append([float(0.2)])
    test_list = []    

#inputs.append(twos_test_inputs)
#
for index in range(len(threes_list)):
    for x in range(len(threes_list[index])):
        for y in range(len(threes_list[index][x])):
            test_list.append(threes_list[index][x][y])
#    threes_test_inputs.append(test_list)
    inputs.append(test_list)
    targets.append([float(0.3)])
    test_list = []
#    
#inputs.append(threes_test_inputs)
#
for index in range(len(fours_list)):
    for x in range(len(fours_list[index])):
        for y in range(len(fours_list[index][x])):
            test_list.append(fours_list[index][x][y])
#    fours_test_inputs.append(test_list)
    inputs.append(test_list)
    targets.append([float(0.4)])
    test_list = []
#    
#inputs.append(fours_test_inputs)
#
for index in range(len(fives_list)):
    for x in range(len(fives_list[index])):
        for y in range(len(fives_list[index][x])):
            test_list.append(fives_list[index][x][y])
#    fives_test_inputs.append(test_list)
    inputs.append(test_list)
    targets.append([float(0.5)])
    test_list = []
#
#inputs.append(fives_test_inputs)
#
for index in range(len(sixes_list)):
    for x in range(len(sixes_list[index])):
        for y in range(len(sixes_list[index][x])):
            test_list.append(sixes_list[index][x][y])
#    sixes_test_inputs.append(sixes_list)
    inputs.append(test_list)
    targets.append([float(0.6)])
    test_list = []
#
#inputs.append(sixes_test_inputs)
#    
network = []
reps = 10000
network = neuro.setup_network(inputs)
neuro.train(network, inputs, targets, reps)
neuro.writeNetworkToFile('Network.net', network)

test_input = [1,1,1,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

test_input_list = []

for items in test_input:
    test_input_list.append(float(items))
    
pred = neuro.predict(network, test_input_list)

#pred = round((pred*10))    

print(pred)
#    
#    
#    inputs = ones_test_list
#    target = [[1], [1], [1], [1], [1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
#    reps = 100
#    network = neuro.setup_network(inputs)
#    neuro.train(network, inputs, target, reps)
#    neuro.writeNetworkToFile('myNetwork.net', network)
    
#for index in range(len(twos_list)):
#    for x in range(len(twos_list[index])):
#        for y in range(len(twos_list[index][x])):
#            test_list.append(twos_list[index][x][y])
#    twos_test_list.append(test_list)
#    test_list = []
#    
#    inputs = twos_test_list
#    target = [[2], [2], [2], [2], [2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2]]
#    reps = 100
#    network = neuro.setup_network(inputs)
#    neuro.train(network, inputs, target, reps)
#    neuro.writeNetworkToFile('myNetwork.net', network)
            
    
