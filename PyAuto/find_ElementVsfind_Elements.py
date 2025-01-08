import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import get_attributes
from selenium.webdriver.support.expected_conditions import title_is

serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://facebook.com')
driver.maximize_window()
element = driver.find_element(By.XPATH,"//input[@id='email']")
element.send_keys('shekharnfe@gmail.com')
time.sleep(6)
print(element.text)
print(element.get_attribute('value'))
driver.quit()