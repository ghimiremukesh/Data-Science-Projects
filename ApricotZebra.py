# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:55:47 2018

@author: cipher
"""
# Spirit Animal: ApricotZebra

# Date Edited: 09/25/2018 

# Challenge #2

#Citations

# lecutre notes from Dr. Jones 

# source for reading file names and count in a directory:
    # https://stackoverflow.com/questions/2632205/how-to-count-the-number-of-files-in-a-directory-using-python

# source for getting the path to read files
    # https://stackoverflow.com/questions/32470543/open-file-in-another-directory-python/32470564
    
import pickle    
import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import sys     # to stop the program after invalid entry. 

list =  os.listdir("scripts")

for i in range(0, len(list)):
     if len(list[i]) == 14:
         series_1 = open(Path("scripts/"+list[i]),"r").read()
     else:
        series_2 = open(Path("scripts/"+list[i]),"r").read()

series_1 = series_1.replace("\n", "")

series_1 = series_1.replace("\t", " ")
series_1 = series_1.replace("    ", " ")
series_1 = series_1.replace("   ", " ")

series_1 = series_1.replace("  ", " ")

series_1 = series_1.split(" ")
del series_1[0]  #it was empty

while '' in series_1:  # too many '' in the list
    series_1.remove('')
  


series_2 = series_2.replace("\n", "")

series_2 = series_2.replace("\t", " ")
series_2 = series_2.replace("    ", " ")
series_2 = series_2.replace("   ", " ")

series_2 = series_2.replace("  ", " ")

series_2 = series_2.split(" ")


while '' in series_2:
    series_2.remove('')


s1_words = []
s2_words = []

for i in range(0, len(series_1)):
        s1_words.append(series_1[i])
        
for i in range(0, len(series_2)):
        s2_words.append(series_2[i])
        

# Working with the sentiment lexicon file

words=[]
scores=[]
file = open('sentiment_lex.csv', 'r')
lex = file.read()
lex = lex.split("\n")
lex.pop() # again empty stuff in list
lex.pop()
for index in range(0, len(lex)):
    lex[index] = lex[index].split(',')

for index in range(0, len(lex)):
    words.append(lex[index][0])
    scores.append(lex[index][1])

scores = np.float64(scores)

negative = []
weakly_negative = []
neutral = []
weakly_positive = []
positive = []
  

for i in range(0, len(scores)):
    if scores[i] < -0.6:
        negative.append(words[i])
    elif scores[i] >= -0.6 and scores[i] < -0.2:
        weakly_negative.append(words[i])
    elif scores[i] >= -0.2 and scores[i] <= 0.2:
        neutral.append(words[i])
    elif scores[i] > 0.2 and scores[i] <= 0.6:
        weakly_positive.append(words[i])
    else:
        positive.append(words[i])

# Now comparing words from series to the sentiment lexicon
        
name = input('Enter series name to analyze the scripts (A or B): ').upper()

if name == 'A':
    series = series_1
elif name == 'B':
    series = series_2
else:
    print('\nInvalid Entry! Enter A or B. Run the program again!\n')
    sys.exit()
    
n_count = 0
wn_count = 0
neu_count = 0
wp_count = 0
p_count = 0

for i in range(0, len(series)):
    for j in range(0, len(negative)):
        if series[i] == negative[j]:
            n_count += 1
            
    for j in range(0, len(weakly_negative)):
        if series[i] == weakly_negative[j]:
           wn_count += 1
           
    for j in range(0, len(neutral)):
        if series[i] == neutral[j]:
           neu_count += 1
    for j in range(0, len(weakly_positive)):
        if series[i] == weakly_positive[j]:
           wp_count += 1
    for j in range(0, len(positive)):
        if series[i] == positive[j]:
           p_count += 1

# Drawing the bar graph
bar_pos = [0,1,2,3,4]
criteria = ['Neg.', 'W.Neg  ', 'Neutral' , 'W. Pos', 'Pos']
script = np.log10([n_count, wn_count, neu_count, wp_count, p_count])
plt.bar(bar_pos, script)
plt.xticks(bar_pos, criteria)
plt.ylabel('log10(word count)')
plt.title('Sentiment Analysis for Series ' + name )
plt.show()

        
        

      

