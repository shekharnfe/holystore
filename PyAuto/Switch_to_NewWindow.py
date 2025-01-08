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

driver.switch_to.new_window('tab')
driver.get('https://amazon.in')
time.sleep(10)

driver.quit()