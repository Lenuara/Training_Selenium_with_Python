from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)
#driver.get('http://automationpractice.com/')
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# локаторы по id и name
driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#локаторы по тексту ссылки и частичному тексту ссылки
#driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()
driver.find_element()

# локаторы classname


driver.close()
driver.quit()




