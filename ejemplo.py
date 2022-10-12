# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:33:07 2022

@author: juana
"""

import cv2
from matplotlib import pyplot as plt
# Lectura de imagen
#imagen = cv2.imread('Material/OpenCV_logo.png')
# Leer en escala de grises -> imagen = cv2.imread('Material/OpenCV_logo.png')
imagen = cv2.imread('Material/retrato.jpg', 0)
imagen = cv2.equalizeHist(imagen)

# Imagen a color
imagenC = cv2.imread('Material/retrato.jpg')
'''
# Crear un histograma
hist = cv2.calcHist(imagen, [0], None, [256], [0,256])
# Graficar el histograma
plt.plot(hist, color = 'gray')
plt.xlabel('Intensidad de iluminación')
plt.ylabel('Canidad de pixeles')
plt.show()
'''

# Histograma a color 
color = ('b','g','r')
# Lee c como los datos para una variable con bgr
for i,c in enumerate(color):
    hist = cv2.calcHist(imagenC, [i], None, [256], [0,256])
    plt.plot (hist, color = c)
    plt.xlim(0,256)
plt.show()
'''
# Guardar la imagen
cv2.imwrite('Material/opencv_1.png', imagen)
'''

# Mostrar la imagen
cv2.imshow('Logo opencv', imagenC)
#Espera a que presionemos la tecla
cv2.waitKey(0)
cv2.destroyAllWindows()









