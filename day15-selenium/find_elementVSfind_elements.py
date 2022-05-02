from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

#######     find_element() - принимает локатор и возвращает один элемент, первый, если найдено несколько
# 1)  Локатор указывает на один элемент
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys('Apple MacBook Pro 13-inch')

# 2) Локатор указывает на несколько элементов
# element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(element.text)

# 3) Элемент может быть недоступен, тогда вывалится исключение NoSuchElementException
# login_element = driver.find_element(By.LINK_TEXT, "Log i")
# login_element.click()

#######     find_elements()
# 1)  Локатор указывает на один элемент, получает один результат - но это коллекция списка
# elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys('Apple MacBook Pro 13-inch') #  AttributeError: 'list' object has no attribute 'send_keys'
# print(len(elements))
# elements[0].send_keys('Apple') # по номеру индекса получаем доступ к эдементу

#2) Локатор указывает на несколько элементов
# elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(len(elements)) # 23
# #print(elements[0].text) # Sitemap
# for i in elements:
#     print(i.text) # напечатает 23 названия ссылки


# 3) Элемент может быть недоступен, ошибки не будет, просто вернет пустой список
elements = driver.find_elements(By.LINK_TEXT, "Log i")
print("elements returned: ", len(elements))

driver.quit()
