from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)

admin=driver.find_element(By.XPATH,"")
user_mgmt=driver.find_element(By.XPATH,"")
users=driver.find_element(By.XPATH,"")
button=driver.find_element(By.XPATH,"")
source=driver.find_element(By.XPATH,"")
target=driver.find_element(By.XPATH,"")
#Mouse hover

act = ActionChains(driver)
act.move_to_element(admin).move_to_element(user_mgmt).move_to_element(users).click().perform()
act.context_click(button).perform()  # perform right click

act.double_click(button).perform()  # perform double click

act.drag_and_drop(source, target).perform() # drag and drop

# suppose if there is an price slider like in ecommerce website, then how can we deal with it.
min_slider=driver.find_element(By.XPATH,"")
max_slider=driver.find_element(By.XPATH,"")
print(min_slider.location)  # it returns dictionary of location like {'x':59,'y':100}
print(max_slider.location)

act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-50,0).perform()

print(min_slider.location)  # it returns dictionary of location like {'x':59,'y':100}
print(max_slider.location)


#Scroll down page by pixel
driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved ",value)

#scroll down page till the element is visible
flag=driver.find_element(By.XPATH,"")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved ",value)

#scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

#scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")




