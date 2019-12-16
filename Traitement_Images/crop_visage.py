# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:19:52 2019

@author: poussanc
"""

import os
# import numpy and matplotlib colormaps
import numpy as np
from PIL import Image


import cv2

#TEST HUGO


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

gray = cv2.imread("image.jpg", 0)
#gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    gray = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = gray[y:y+h, x:x+w]
        
cv2.imshow('img',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


#FIN TEST HUGO

#
## main
#path_base="E:\\COURS\\PROJ 942\\Partie_1_Python\\Traitement_Images\\Base_visages"
#path_images="E:\\COURS\\PROJ 942\\Partie_1_Python\\Proj942\\Traitement_Images\\test"
##[X,y] = read_images (path_base)
#
###############
## perform a full pca
## D = eigenvalues , W = eigenvectors , mu = mean
##[D, W, mu] = pca ( asRowMatrix(X), y)
#
###############
#list_images=os.listdir(path_images)
#ind=0
## reading an image
#for a in list_images:
#    path_image = path_images+"\\"+a # image à tester
#    im_orig = cv2.imread(path_image)
#    height, width, depth = im_orig.shape
#    print(height, width, depth)
#    cv2.imshow('original',im_orig)
#    cv2.waitKey(0)
#    
#    # parametres du cadre défini sur la tablette
#    left=int(0.16*width)
#    top=int(0.07*height)
#    right=int(0.89*width)
#    bottom=int(0.75*height)
#    
#    #resize
#    im = Image.open(path_image)
#    imtest=im.crop((left,top,right,bottom))
#    imtest=imtest.resize((92,112))
#    imtest = imtest.convert ("L")
#    imtest.save(str(ind)+".jpg")
#    test = np.asarray (imtest , dtype =np.uint8 )
#    cv2.imshow(path_image,test)
#    cv2.waitKey(0)
#    # model computation
#    model = EigenfacesModel (X , y)
#    print("predicted =", model.predict(test))
#    ind+=1
#    
#    #cv2.destroyAllWindows()