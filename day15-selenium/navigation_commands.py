# back()    forward()   refresh()  ====> доступ напрямую через экземпляр драйвера
####################################
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)

driver.get('http://automationpractice.com/')
driver.get('https://opensource-demo.orangehrmlive.com/')

driver.back()   # http://automationpractice.com
driver.forward()   # https://opensource-demo.orangehrmlive.com/

driver.refresh()

driver.quit()