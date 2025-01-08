import navmenu
from Tools.scripts.objgraph import externals
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_is

serv_obj=Service('D:\Drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://holystore.in')

driver.find_element(By.LINK_TEXT,"Login").click()
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"pass").send_keys("bedwipro@123")
driver.find_element(By.CLASS_NAME,"btn btn-warning w-100 py-2").click()
driver.close()
#CSS Selectors
#tag id   tagname#valueofId   input#email
#tag class tagname.valueOfClass input.inputtext _55r1 _6luy _9npi or tagname.valueOfClass input.inputtext
#tag attribute tagname[attribute=value] other than ID and Class we can take other attributes
#tag class attribute input.inputtext[data-testid=royal_pass]


#Tutorial 5

# get commands or application commands
# 1. title -- to capture title of current webpage (driver.title)
# 2. current_url -- to capture url of current webpage (driver.current_url)
# 3  page_source -- to capture source code of the page (driver.page_source)


# conditional commands
# 1. is_displayed()
# 2. is_enabled()
# 3. is_selected() -- radio buttons and check boxes


# browser commands
# close -- process will not killed in backend , only one browser close, it only close first browser or parent browser
#where driver focuses
# quit() -- All browsers close and process killed



# navigational commands
# 1. back()
# 2. forward()
# 3. refresh()



#text vs get_attribute('value')


# time.sleep() -- performance of the script is very poor.
 #               if the element is not available within the time mentioned , still there is chance of getting exception.


# wait commands
# 1. implicit wait -- performance will not be reduced(if the element is available within the time , it proceed to execute further statements.
# 2. explicit wait




#Checkboxes

#checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")


# Approach 1
# for i in range(len(checkboxes)):
#    checkboxes[i].click()

#  Approach 2
#for checkbox in checkboxes:
#       checkbox.click()


# Select multiple checkboxes by choice
for checkbox in checkboxes:
       weekname=checkbox.get_attribute('id')
       if weekname=='Monday' or weekname=='sunday':

            checkbox.click()


# Select last 2 checkboxes
#for i in range(len(checkboxes)-2,len(checkboxes)):  range(5,7) --> 6,7
#       checkboxes[i].click()

# Select first 2 checkboxes
#for i in range(len(checkboxes))
#    if i<2:
#       checkboxes[i].click()



#time.sleep(5)

#Clearing all the checkboxes
#for checkbox in checkboxes:
#   if checkbox.is_selected():
#       checkbox.click()


# Links
# 1. internal
# 2. external
# 3. broken link


#Frame/IFrame

 # These all are selenium 4 commands
#switch_to.frame(name of the frame)
#switch_to.frame(id of the frame)
#switch_to.frame(webelement)
#switch_to.frame(0)  -- index

