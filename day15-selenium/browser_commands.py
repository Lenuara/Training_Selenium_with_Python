import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)

#driver.close() # закрывает только то окно, которое было открыто через get, процессы не завершаются
driver.quit() # закрывает все окна браузера и завершает все процессы

