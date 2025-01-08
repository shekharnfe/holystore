import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://amazon.in')
driver.maximize_window()

#open alert window
driver.find_element(By.XPATH,"//button[normalize-space()='click for js prompt']").click()
time.sleep(5)

myalrt = driver.switch_to.alert
print(myalrt.text)

myalrt.send_keys("welcome")
myalrt.accept() #close alert window by using ok button
myalrt.dismiss() #close alert window by using cancel button


# Authentication popup
# inject username and password in url

# Syntax-- https://admin:admin@url



