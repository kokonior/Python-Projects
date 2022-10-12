# -*- coding: utf-8 -*-
"""
Created on Tue May 24 15:14:20 2022

@author: juana
"""

import cv2
import numpy as np

# Lectura de imagen
imagen = cv2.imread('Material/Colores.png')
imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Rangos de colores a buscar
amarilloBajo = np.array([20,100,20], np.uint8)
amarilloAlto = np.array([30,255,255], np.uint8)



# Mascara de color 
moradoBajo = np.array([130,100,20], np.uint8)
moradoAlto = np.array([150,255,255], np.uint8)


maskAmarillo = cv2.inRange(imagenHSV, amarilloBajo, amarilloAlto)
maskMorado = cv2.inRange(imagenHSV, moradoBajo, moradoAlto)


# Encontrar contornos

# Mostrar imagen
cv2.imshow('logo opencv', imagen)
cv2.imshow('Mascara Amarillo', maskAmarillo)
cv2.imshow('Mascara Amarillo', maskMorado)
cv2.waitKey(0)
cv2.destroyAllWindows()