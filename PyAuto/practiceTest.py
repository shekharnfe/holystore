import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys('selenium')
driver.find_element(By.XPATH,"//input[@type='submit' and @class='wikipedia-search-button']").click()
all_links = driver.find_elements(By.XPATH,"//div[@class='wikipedia-search-results']//a")

for i in all_links:
    print(i.text)

driver.close()