# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:58:10 2022

@author: juana
"""

import cv2
from matplotlib import pyplot as plt

imagen = cv2.imread ('Material/colores.png', 0)

imagenA = cv2.imread ('Material/ruido.jpg', 0)

_, th1 = cv2.threshold(imagen, 150, 255, cv2.THRESH_BINARY)

_, th2 = cv2.threshold(imagenA, 150, 255, cv2.THRESH_OTSU)
# Mostrar imagen
cv2.imshow('Colores', imagen)
cv2.imshow('Binarizado simple', th1)
cv2.imshow('Binarizado otsu', th2)
cv2.waitKey(0)
cv2.destroyAllWindows()