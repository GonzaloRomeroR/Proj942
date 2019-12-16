# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:55:42 2019

@author: poussanc
"""

from reconnaissance_visage import *

path="E:\\COURS\\PROJ 942\\Partie_1_Python\\Proj942\\Traitement_Images\\test"
path_base="E:\\COURS\\PROJ 942\\Partie_1_Python\\Proj942\\Traitement_Images\\Base_visages"
list_images=os.listdir(path)
ind=0
for a in list_images:
    path_image = path+"\\"+a # image à tester
    im = cv2.imread(path_image)
    res=reconnaissance_visage(path_base,path_image)
    print a+" : "+res