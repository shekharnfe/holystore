# Alerts/popups


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

# if frame is linked each other
driver.switch_to.frame("framename")
driver.find_element(By.LINK_TEXT,"linkname").click()
driver.switch_to.default_content()  # go back to main page

driver.switch_to.frame("secondframename")
driver.find_element(By.LINK_TEXT,"linkname").click()
driver.switch_to.default_content()  # go back to main page

driver.switch_to.frame("thirdframename")
driver.find_element(By.LINK_TEXT,"linkname").click()

# driver cannot switch directly one frame to another frame

# INNER FRAMES

# Frame inside a frame  and when name and id is not available of frame
outerframe = driver.find_element(By.XPATH,"//iframe[@src='frames.html']")
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH,"//iframe[@src='innerframes.html']")
driver.switch_to.frame(innerframe)

#then identify the element
driver.switch_to.parent_frame()