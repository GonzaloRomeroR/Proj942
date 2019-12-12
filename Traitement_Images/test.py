# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:55:42 2019

@author: poussanc
"""

from reconnaissance_visage import *
path_base="E:\\COURS\\PROJ 942\\Partie_1_Python\\Proj942\\Traitement_Images\\Base_visages"
path_image_test='hugo.jpg'
res=reconnaissance_visage(path_base,path_image_test)
print res