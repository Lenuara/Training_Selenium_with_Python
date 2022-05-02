from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get('http://automationpractice.com/')
#driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# используем локаторы по имени класса
s=driver.find_elements(By.CLASS_NAME, "homeslider-container")
print(len(s))  # 5 - количество слайдов в слайдере

t=driver.find_elements(By.TAG_NAME, "a")
print(len(t)) # 149 - количество ссылок на главной странице


driver.close()
driver.quit()