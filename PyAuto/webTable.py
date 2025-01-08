from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

#Total no. of rows and columns
table_row=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
table_col=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th")


print(len(table_row))
print(len(table_col))

# read specific row and column data
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[6][1]")
print(data.text)

data1=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[6]/td[1]")
print(data1.text)

# read all the  rows and column data
for r in range(2, table_row+1):
    for c in range(1, table_col+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end='  ')

# # read data based on condition
for r in range(2,table_row+1):
    author=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author=="Mukesh":
        book=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        print(book)

driver.close()
