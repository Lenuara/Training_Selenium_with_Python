import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)

driver.get('https://itera-qa.azurewebsites.net/home/automation')
driver.maximize_window()

# 1) выберем один флажок на чекбоксе
#driver.find_element(By.XPATH, "//input[@id='monday']").click()

# 2) выберем несколько флажок на чекбоксе
checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes)) #7

        # 1 способ
# for i in range(len(checkboxes)):
#     checkboxes[i].click()
#
#         # 2 способ
# for checkbox in checkboxes:
#     checkbox.click()

# 3) выборочная отметка флажков
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#         checkbox.click()

# 4) поставить последние два флажка снизу
# for i in range(len(checkboxes)-2, len(checkboxes)): # дает нам интервал range(5,7) --> это 6 и 7 флажок фактически из списка
#     checkboxes[i].click()

# 5) поставить первые два флажка
# for i in range(len(checkboxes)): # дает нам интервал range(5,7) --> это 6 и 7 флажок фактически из списка
#     if i<2:
#         checkboxes[i].click()

# 6) снять все флажки с проверкой выбран ли он
for checkbox in checkboxes: # сначала установим все флажки
    checkbox.click()
time.sleep(5)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()













#driver.quit()