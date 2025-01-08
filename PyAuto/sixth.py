import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests as requests
serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://snapdeal.com')
driver.maximize_window()
links=driver.find_elements(By.XPATH,"//a")
count=0
print(len(links))
#for i in links:
 #   print(i.text)
for i in links:
    url=i.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None

    if res.status_code<=400:
        print(url,"This is normal link")
    else:
        print(url, "This is broken link")
        count=count+1
print("Total no.of broken links :" ,count)
driver.quit()


