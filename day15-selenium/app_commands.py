from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)
#driver.get('http://automationpractice.com/')
driver.get('https://opensource-demo.orangehrmlive.com/')
#driver.maximize_window()
# ---- доступ к методам через экземпляр вебдрайвера-----
print(driver.title)  # OrangeHRM
print(driver.current_url)  # https://opensource-demo.orangehrmlive.com/
print(driver.page_source)

driver.close()
driver.quit()



