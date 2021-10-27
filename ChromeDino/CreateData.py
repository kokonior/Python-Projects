import cv2
import os
import keyboard
from utils.grabscreen import grab_screen

count = 0
pic = 1

# Point to where we want the images to be saved
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "img\\")

# Collets images until you press e
while not keyboard.is_pressed("e"):

    # You need to define the pixels you want to grab here!
    image = grab_screen(region=(85, 350, 715, 500))
    #Covert to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Cover to black or white pixel
    (thresh, image) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Bot View', image)
    cv2.waitKey(1)

    # Can adjust to save more or less pictures. 
    # Currently save one pic every 50 times through loop
    if count % 50 == 0:
        cv2.imwrite(f"{path}BotView{pic}.jpg", image)
        print(f"Saved Picture numder: {pic}")
        pic += 1

    count += 1