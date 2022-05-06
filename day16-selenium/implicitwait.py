# implicit - скрытый, неявный
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)
# добавляем в начало и будет применяться ко всем командам ниже
driver.implicitly_wait(10) # максимум 10 сек либо пока элемент не будет доступен

searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys('Selenium')
searchbox.submit()

# один из способов задержки в секундах - метод пайтона
# ждем 5 сек
#time.sleep(5)

# через заголовки найдем ссылку конкретно с текстом "Selenium"
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver.quit()
