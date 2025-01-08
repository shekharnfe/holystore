import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get('https://text-compare.com/')
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//*[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//*[@id='inputText2']")

input1.send_keys("Welcome to selenium")

act=ActionChains(driver)
act.key_down(Keys.CONTROL)  # Ctrl+A
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

act.key_down(Keys.CONTROL)  # Ctrl+C
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

act.send_keys(Keys.TAB)   # press tab key
act.perform()

act.key_down(Keys.CONTROL)  # Ctrl+V
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

time.sleep(5)

driver.close()


