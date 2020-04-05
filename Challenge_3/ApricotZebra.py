# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 12:24:12 2018

@author: cipher

"""
# Spirit Animal: ApricotZebra

# Challenge 3
# Last Edited: 10/12/2018

# sources: class wiki for average image calcualtion

# source for getting the path to read files
    # https://stackoverflow.com/questions/32470543/open-file-in-another-directory-python/32470564


import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from pathlib import Path 

check = True
while check:
    threshold = np.float64(input("Enter a threshold value (0 - 255): "))
            
    if (threshold >= 0 and threshold <= 255):
        check = False
        list_of_images = os.listdir("starbucks")
        images = []
        avg_img=[]
        std_img = []
        std_sum = 0
        
        for i in range(0, len(list_of_images)):
            img = Image.open(Path("starbucks\\"+list_of_images[i]))
            images.append(img)
            img = np.float64(img)
            try:
                avg_img = avg_img + img 
            except:
                avg_img = img
               
        avg_img /= len(list_of_images)
        
        for image in images:
            std_sum = std_sum + ((avg_img-image)**2)
        
        std_img = np.sqrt(std_sum/len(list_of_images))
        
        
        for row in range(0, len(avg_img)):
            for col in range(0, len(avg_img[row])):
                if (std_img[row][col] > threshold).any():
                    avg_img[row][col] = [255, 0, 0]
        
        
        avg_img = np.clip(avg_img, 0, 255)
        std_img = np.clip(std_img, 0, 255)
        avg_img = np.uint8(avg_img)
        
        plt.imshow(avg_img)
        plt.show()
        
    else:
        print("Please enter the threshold in the given range. 0 - 255! The program will restart!")
        check = True

        
    