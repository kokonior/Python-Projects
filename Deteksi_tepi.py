from scipy import ndimage
import cv2
import numpy as np

def sobel (img):
    im = img.astype('int32')
    gx = ndimage.sobel(im, 1)
    gy = ndimage.sobel(im, 0)

    magnitude = np.hypot(gx, gy)
    magnitude = magnitude*255 / np.max(magnitude)

    cv2.imwrite('sobel.png', magnitude)

def prewitt(img):
    im = img.astype('int32')
    gx = ndimage.prewitt(im, 1)
    gy = ndimage.prewitt(im, 0)

    magnitude = np.hypot(gx, gy)
    magnitude = magnitude * 255 / np.max(magnitude)

    cv2.imwrite('prewitt.png', magnitude)

def canny(img, th1, th2):
    can = cv2.Canny(img, th1, th2)
    cv2.imwrite('canny.png', can)

image = cv2.imread('File/Monalisa.PNG', 0)
sobel(image)
prewitt(image)
canny(image, 90, 200)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
