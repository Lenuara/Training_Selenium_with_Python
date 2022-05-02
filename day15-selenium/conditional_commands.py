from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

# is_displayed()  is_enabled()  --- доступ к методам через веб-элемент страницы

# searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# print("Displayed status: ", searchbox.is_displayed()) # True
# print("Enabled status: ", searchbox.is_enabled())   # True

# is_selected   -for radiobuttons and checkboxes
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")
print("Cостояние радиокнопок по умолчанию.........." )
print(rd_male.is_selected()) # False
print(rd_female.is_selected()) # False

print("После выбора радиокнопки male.........." )
rd_male.click()
print(rd_male.is_selected()) # True
print(rd_female.is_selected()) # False

print("После выбора радиокнопки female........." )
rd_female.click()
print(rd_male.is_selected()) # False
print(rd_female.is_selected()) # True

driver.quit()