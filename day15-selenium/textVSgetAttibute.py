from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get('https://admin-demo.nopcommerce.com/login')
driver.maximize_window()

emailbox = driver.find_element(By.XPATH, "//input[@id='Email']")
# в поле ввода емайла есть значение по умолчанию, его нужно стереть, иначе новое добавится в конец
emailbox.clear()
emailbox.send_keys('abc@abcd.com')
# .text - забираем внутренний текст между тегами
print('resut of text:',emailbox.text) #- ничего не вернет, так как нет внутреннего текста

print('resut of get_attribute:',emailbox.get_attribute('value')) # забирает значение атрибута value

