from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)

driver.get('http://facebook.com/')
driver.maximize_window()

#tag and id
#driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

#tag and class
#  если несколько классов, то найдет первый элемент, т.к. find_elemenT
#driver.find_element(By.CSS_SELECTOR, "input.inputtext ").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR, ".inputtext ").send_keys("abc")

#tag and attribute
#driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abc")

#tag and class and attribute
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("abc")






