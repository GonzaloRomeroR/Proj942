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


# main
path_base="E:\\COURS\\PROJ 942\\Partie_1_Python\\Traitement_Images\\Base_visages"
path_images="E:\\COURS\\PROJ 942\\Partie_1_Python\\Base_visages"
#[X,y] = read_images (path_base)

##############
# perform a full pca
# D = eigenvalues , W = eigenvectors , mu = mean
#[D, W, mu] = pca ( asRowMatrix(X), y)

##############
list_images=os.listdir(path_images+"\\s12")
ind=0
# reading an image
for a in list_images:
    path_image = path_images+"\\s12\\"+a # image à tester
    im_orig = cv2.imread(path_image)
    height, width, depth = im_orig.shape
    print(height, width, depth)
    cv2.imshow('original',im_orig)
    cv2.waitKey(0)
    
    # parametres du cadre défini sur la tablette
    left=int(0.16*width)
    top=int(0.07*height)
    right=int(0.89*width)
    bottom=int(0.75*height)
    
    #resize
    im = Image.open(path_image)
    imtest=im.crop((left,top,right,bottom))
    imtest=imtest.resize((92,112))
    imtest = imtest.convert ("L")
    imtest.save(str(ind)+".jpg")
    test = np.asarray (imtest , dtype =np.uint8 )
    cv2.imshow(path_image,test)
    cv2.waitKey(0)
    # model computation
    model = EigenfacesModel (X , y)
    print("predicted =", model.predict(test))
    ind+=1
    
    #cv2.destroyAllWindows()