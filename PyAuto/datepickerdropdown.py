import time
from os import times


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='dob']").click()

datepicker_mon = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
datepicker_mon.select_by_visible_text("Jul")

datepicker_yr=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
datepicker_yr.select_by_visible_text("1982")

alldates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for dte in alldates:
    if dte.text=="2":
        dte.click()
        break

time.sleep(6)
driver.close()

