
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support.events import EventFiringWebDriver ,AbstractEventListener
from datetime import date, datetime,time
import pyautogui
import time

Weekday = datetime.today().weekday() # mon=0 ...sun=6
Cur_Url =""

# set Webdriver default options
opts = Options()
opts.add_argument("user-data-dir=~/.config/google-chrome/Default") 
opts.add_argument("--disable-notifications")
opts.add_argument("--disable-popup-blocking")
opts.add_argument('--no-sandbox')
opts.add_argument("--incognito")
opts.add_argument("start-maximized")

opts.add_experimental_option("prefs",{
    #disable cam & audio
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
})
# opts.add_experimental_option("prefs",{
#     # able cam & audio
#     "profile.default_content_setting_values.media_stream_mic": 1, 
#     "profile.default_content_setting_values.media_stream_camera": 1,
# })

driver = webdriver.Chrome("/home/jason/Desktop/Webdriver_test/chromedriver" , chrome_options=opts)


UserName = "Your_Email"
UserPass = "Your_Password"


class Class_Obj:
    Class_num = 0
    Class_Time_List = []
    Today_Class = []
    Subject={}

def Import_Json():
    import json
    try:
        with open('Class_information01.json') as json_file:
            Data = json.load(json_file)
            Class_Obj.Class_num = Data['N']
            Class_time = Data['class_time']
            Class_Obj.Today_Class = Data['Week'][str(Weekday)]
            Class_Obj.Subject = Data['subject']
            
            for i in range(Data['N']):
                S_=Class_time[str(i)]['start_hour']*60+Class_time[str(i)]['start_min']
                E_=Class_time[str(i)]['end_hour']*60+Class_time[str(i)]['end_min']
                Class_Obj.Class_Time_List.append((S_,E_))
    except Exception as exc:
        print('Check yout JSON file ')
        print('ERROR : '+exc)


class Check_Listener(AbstractEventListener):
    # For checking Class is open or not
    def after_click(self, element, driver):
        Cur_Url=driver.current_url
        print(driver.current_url)

def Login_User():
    #By using incognito mode , it require Login
    try:
        time.sleep(2)
        driver.get("https://accounts.google.com/") 
        time.sleep(2)
        broswer = driver.find_element_by_id('identifierId')
        broswer.send_keys(UserName)

        time.sleep(1)
        broswer = driver.find_element_by_class_name('VfPpkd-vQzf8d').click()
        time.sleep(3)

        broswer = driver.find_element_by_name('password')
        broswer.send_keys(UserPass)
        

        time.sleep(2)
        broswer = driver.find_element_by_class_name('VfPpkd-vQzf8d').click()
        print('Login')
    except:
        print("Try using GCP account or reconnecting your Internet")


def Current_Day(Auto_Close:bool):
    ith =Current_Class()
    if(ith==Class_Obj.Class_num):
        print("Off School !")
        return
    for i in range(ith,Class_Obj.Class_num):
        
        Meeting(Class_Obj.Today_Class[ith])
        wait_time = Class_Obj.Class_Time_List[ith][1]-datetime.now().hour*60 -datetime.now().minute 
        time.sleep(wait_time*60)

        if Auto_Close:
            driver.close()
        
def Current_Class():
    Now_min = datetime.now().hour*60 + datetime.now().minute
    Class_Time_List = Class_Obj.Class_Time_List
    ith=0
    found=False
    
    for C in Class_Time_List:
        if(Now_min <=C[1]):
            found=True
            break
        ith+=1
    if found: return ith
    else :return Class_Obj.Class_num

def Join():
    time.sleep(5)
    pyautogui.click(1160,685) 
    #I can't close the block so I use some pyautogui 
    print('close block')
    time.sleep(2)
    driver.find_element_by_class_name("NPEfkd.RveJvd.snByac").click()


def Instant_Meet(Meet_Url:str):
    time.sleep(5)
    temp_script = 'window.open("'+Meet_Url+'", "_blank");'
    print(temp_script)
    driver.execute_script(temp_script)
    driver.switch_to_window(driver.window_handles[1])
    Join()


def Meeting(cur_subject:str):
    try:
        time.sleep(5)
        Meet_url = "https://meet.google.com/"
        Cur_Url = Meet_url
        driver.execute_script('''window.open("https://meet.google.com/", "_blank");''')
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(1)

        L_driver = EventFiringWebDriver(driver,Check_Listener())
        #sent code
        broswer = L_driver.find_element_by_id('i3')
        broswer.send_keys(Class_Obj.Subject[cur_subject])
        
        while(Cur_Url==Meet_url):
            #try join until class open
            time.sleep(3)
            L_driver.find_element_by_class_name('VfPpkd-vQzf8d').click()
        
        Join() #close popout and join
        print('Join '+cur_subject+' Class !')
    except:
        print('Reconnect your wifi !')


def test(): #For testing new tab work all right
    time.sleep(2)
    driver.get("https://www.youtube.com/")
    time.sleep(1)
    driver.execute_script('''window.open("https://meet.google.com/", "_blank");''')
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(1)
    driver.find_element_by_tag_name('body').send_keys('/')
    driver.send_keys("https://meet.google.com/")
    
# main code

Import_Json()
Login_User()
Current_Day(True) # Auto_Close:True 

# Instant_Meet("Meet_Url")

