import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import get_attributes
from selenium.webdriver.support.expected_conditions import title_is

serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://snapdeal.com')
driver.maximize_window()
#elements=driver.find_elements(By.XPATH,"//div[@class='col-xs-5']//a")
elements=driver.find_elements(By.XPATH,"//div[@class='footer-inner']//a")
time.sleep(6)
for i in elements:

    print(i.text)
