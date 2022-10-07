# pip install PyQRCode

import PIL
import pyqrcode
from pyqrcode import QRCode

generateData = input("enter text to convert :")
imageName = input("enter image name to save :")
imageNameResult = imageName + ".png"
url = pyqrcode.create(generateData)

url.png(imageNameResult, scale=6)
