import os             
import pyautogui
import pytesseract
from PIL import Image
import pickle
from time import sleep
import requests
import json

#(120,150)
#(375,530)

try:
    os.startfile("C://Users//99ans//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Microsoft Teams.lnk") # open MS Teams application
    sleep(10)
except Exception as e:
    print(e)

def transform(s):
    l = s.split("\n") #split by new line
    l = list(filter(lambda x: x != "", l)) #remove empty items
    return l

def loadOld():
    with open("oldContent.pickle","rb") as f:
        return pickle.load(f)
        
def createOrReplaceOld(content):
    with open("oldContent.pickle","wb") as f:
        pickle.dump(content,f)

    
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\99ans\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

while(1>0):
    image = pyautogui.screenshot()
    # Setting the points for cropped image. Depends on laptop screen size
    left = 120
    top = 150
    right = 375
    bottom = 530
      
    # Cropped image of above dimension
    # (It will not change orginal image)
    image = image.crop((left, top, right, bottom))
    #image.show()
    
    s = pytesseract.image_to_string(image)

    newContent = transform(s)
    try:
        oldContent = loadOld()
    except Exception as e:
        createOrReplaceOld(newContent)
        oldContent = loadOld()
        
    if oldContent!=newContent:
        print("New message")
        print(oldContent)
        print(newContent)
        createOrReplaceOld(newContent)
        
        url = ''
        myobj = {'text': 'New message'}

        x = requests.post(url, data = json.dumps(myobj))
        print(x)
        
    else:
        print("No new messages")

    sleep(30)
