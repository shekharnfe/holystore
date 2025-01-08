import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://google.com')
driver.maximize_window()
element = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
element.send_keys('Selenium')
element.submit()

driver.find_element(By.XPATH,"//h3[text(),'Selenium'").click()
time.sleep(10)
driver.close()