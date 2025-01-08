import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_is

serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://amazon.in')
time.sleep(5)
driver.get('https://flipkart.com')
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
driver.refresh()
driver.quit()