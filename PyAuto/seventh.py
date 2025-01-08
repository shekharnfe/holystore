import time
from time import sleep

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests as requests
from selenium.webdriver.support.select import Select

serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://snapdeal.com')
driver.maximize_window()
drpcount = driver.find_element(By.XPATH,"//select[@id='input country']")
drp=Select(drpcount)

#select option from dropdown
drp.select_by_visible_text("India")
drp.select_by_value("10")
drp.select_by_index(13) # Manually count the options
all_options=drp.options
print(len(all_options))

for i in all_options:
    print(i.text)


# select option from the dropdown without built in function
for i in all_options:
    if i.text=="India":
        i.click()
        break

