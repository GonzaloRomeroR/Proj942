# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt


# reading an image
#im = cv2.imread('Bill_Gates.jpg')
#height, width, depth = im.shape
#print(height, width, depth)
#cv2.imshow('original',im)
#cv2.waitKey(0)
#
## Filtering example
#kernel = np.ones((5,5),np.float32)/25
#im_filt = cv2.filter2D(im,-1,kernel)
#cv2.imshow('filtered',im_filt)
#cv2.waitKey(0)
#
## Crop example
##
#im_cropped = im[20:120, 40:160]
#cv2.imshow('cropped image',im_cropped)
#cv2.waitKey(0)
#
## Profile plot example
#x0 = width//2
#profil_vert = im[:,x0,1]
#plt.plot(profil_vert)
#plt.ylabel('vertical profile')
#plt.show()
#im[:,x0] = [0,0,255]
#cv2.imshow('image with line',im)
#cv2.waitKey(0)
#
#cv2.destroyAllWindows()

#def detect_visage2(img):
#    height, width, depth = img.shape
#    top,bot,left,right=0,0,0,0 #initialisiation des bords du crop
#    # calcul du point haut de la tete (on suppose qu'il se trouve vers le milieu de l'image)    
#    lign_vert=img[:,width//2,1] # parcours selon le profil vertical
#    i=0
#    while (i<height or top==0):
#        if abs(lign_vert[i+1]-lign_vert[i])>20:
#            top=i
#        else:
#            i=i+1
#    # calcul des points gauche et droite du visage
#    lign_hor=img[top+,:,1] # parcours selon le profil vertical
#    i=0
#    while (i<width or top==0):
#        if abs(lign_vert[i+1]-lign_vert[i])>20:
#            top=i
#        else:
#            i=i+1
#    bot=round((right-left)*(4/3))

def detect_visage(name_img):
    img=cv2.imread(name_img,0)
    height, width = img.shape
    top,bot,left,right=0,0,0,0 #initialisiation des bords du crop
    # calcul du point haut de la tete (on suppose qu'il se trouve vers le milieu de l'image)    
    for i in range(height-1):
        for j in range(width-1):
            if abs(img[i,j+1]-img[i,j])>10:
                top=i
                break
        if top!=0:
            break
    # calcul des points gauche et droite du visage
    axe_h=0
    var0=width
    for i in range(top,height-1):
        for j in range(width-2):
            if abs(img[i,j+1]-img[i,j])>50:
                var1=j
                if var1>var0:
                    left=j-5
                    axe_h=i
                    print(j)
                    break
                else:
                    var0=var1
        if left!=0:
            break
    
#    lign_h=img[axe_h,left:] 
#    j=len(lign_h)-1
#    while (j>1 or right==0):
#        if abs(lign_h[j-1]-lign_h[j])>20:
#            right=j
#        else:
#            j=j-1
    right=200
    #calcul du point du bas
    bot=round((right-left)*(4/3))+top
    # resize image
    im = cv2.imread(name_img)
    im_crop = im[top:bot,left:right]
    cv2.imshow('cropped image',im_crop)
    cv2.waitKey(0)
    

detect_visage('Bill_Gates.jpg')
       
  
  
  