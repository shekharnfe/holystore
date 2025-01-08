import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import os
location=os.getcwd()
from KeyboardAction import driver

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)

    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

driver1=chrome_setup()
driver1.get('https://www.videolan.org/vlc/download-windows.html')
driver1.maximize_window()
driver1.find_element(By.XPATH,"//b[normalize-space()='VLC']").click()
time.sleep(5)
driver1.close()