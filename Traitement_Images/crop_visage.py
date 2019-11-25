# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:19:52 2019

@author: poussanc
"""


import cv2


# reading an image
path_image = 'Bill_Gates.jpg'
im_orig = cv2.imread(path_image)
height, width, depth = im_orig.shape
print(height, width, depth)
cv2.imshow('original',im_orig)
cv2.waitKey(0)

# parametres du cadre
left=70
top=15
right=145
bottom=110

# image resized
im=im_orig[top:bottom,left:right]
cv2.imshow('resized',im)
cv2.waitKey(0)

