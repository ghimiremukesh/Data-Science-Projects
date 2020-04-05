# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:34:45 2018

@author: ApricotZebra
"""
# Spirit Animal: ApricotZebra

# Date Edited: 09/13/2018

# Challenge 0.5


# sources: https://discuss.codecademy.com/t/how-to-make-text-italic-in-python/24902
# article: https://muse-jhu-edu.umiss.idm.oclc.org/article/509324/pdf

# What does the future hold for this extinct zebra?
# Heywood, P. (2013). The Quagga and Science: What Does the Future Hold for This Extinct Zebra? Perspectives in Biology and Medicine, 56(1), 53-64. doi:10.1353/pbm.2013.0008


from PIL import Image as img
from IPython.display import display

print("\n\t\tLearn about my Spirit Animal")
print("\n")
print("\t\t\tZebra")

# open image and display in spyder's console
a = img.open("zebra.jpg")
width, height = a.size
a2 = a.resize((int(width/4), int(height/4)))

display(a2)

print("\n\t\tTaxonomic Classification\n")
print("COMMON NAME:\tPlains zebra\n"
      "KINGDOM    :\tAnimalia\n"
      "PHYLUM     :\tChordata\n"
      "CLASS      :\tMammalia\n"
      "ORDER      :\tPerissodactyla\n"
      "FAMILY     :\tEquidae\n"
      "GENUS      :\t\x1B[3mEquus\x1B[23m (horse)\n" 
      "SPECIES    :\t\x1B[3mquagga\x1B[23m\n")

input("Press any key to view more.........")

print("\n\n\t\t\tDID YOU KNOW??\n")
print("* Quaggas HAD A STRIKING APPEARANCE: the face, neck, and anterior part of"
      "their bodies had white stripes like zebras, but unlike other zebras, their legs"
      "were not striped.The remainder of the quagga and the background color in the"
      "areas with white stripes was a brownish color, sometimes described as light"
      "brown, reddish-brown, or yellowish-brown")

print("\n\n* In the 20th century, tissue from a quagga yielded the first DNA of an"
      "extinct organism to be cloned and sequenced.")

print("\n\n* and lastly, this animal was extinct in the 19th century. ):")

print("\n\nThat's all for now! Bye Bye!")




