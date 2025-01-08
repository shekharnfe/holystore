from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service('D:\Drivers\chromedriver_win32\chromedriver.exe')
    ops=webdriver.ChromeOptions()
    ops.headless=True

    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return  driver


def headless_edge():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service('D:\Drivers\edgedriver_win64\msedgedriver.exe')
    ops=webdriver.EdgeOptions()
    ops.headless=True

    driver = webdriver.Edge(service=serv_obj,options=ops)
    return  driver



mydriver=headless_chrome()
mydriver.get('https://facebook.com')
print(mydriver.title)
print(mydriver.current_url)
mydriver.close()