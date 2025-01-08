import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import get_attributes
from selenium.webdriver.support.expected_conditions import title_is
import os

serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get('https://facebook.com')
driver.maximize_window()

forgotpwd=Keys.CONTROL+Keys.RETURN
driver.find_element(By.LINK_TEXT,"Forgotten password?").send_keys(forgotpwd)
time.sleep(10)

#opens a new tab and switches to new tab




driver.quit()