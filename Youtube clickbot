from selenium import webdriver
import time
import os
from selenium.common.exceptions import NoSuchElementException
from tkinter import *
from tkinter import font as font
from threading import Thread

def maininmain():
  print("Generating")
  url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  while:
       time.sleep(1)
       os.popen(r'C:\Coding\TorBrowser\Browser\firefox.exe')
       time.sleep(6)
       PROXY = "socks5://localhost:9150"
       options = webdriver.ChromeOptions()
       options.add_argument('--proxy-server=%s' % PROXY)
       driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Coding\Bots\chromedriver.exe')
       driver.get(url)
       time.sleep(3)
       try:
           elem = driver.find_element_by_id("captcha-page")
           print(elem)
           time.sleep(1)
           pass
       except NoSuchElementException:
           pass
       time.sleep(1)
       try:
           elem = driver.find_element_by_id("captcha-form")
           print(elem)
           time.sleep(1)
           pass
       except NoSuchElementException:
           pass
       time.sleep(1)
       try:
           elem = driver.find_element_by_xpath("//form/div/div/button")
           print(elem)
           elem.click()
       except NoSuchElementException:
           pass
       time.sleep(1)
       time.sleep(18)
       os.system(r'TASKKILL /F /IM firefox.exe')
       os.system(r'TASKKILL /F /IM chrome.exe')
       time.sleep(3)
