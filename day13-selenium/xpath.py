# xpath - это xml -путь для поиска на основе структуры DOM
#
#/html/body/nav/div/div[2]/ul[3]/li[1]/a
#//*[@id="header-navbar"]/ul[3]/li[1]/a

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get('http://automationpractice.com/')
#driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# Absolute xpath
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys('T-shirts')
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

# Relative xpath
# driver.find_element(By.XPATH, "//*[@id='search_query_top']").send_keys('T-shirts')
# driver.find_element(By.XPATH, '//*[@id="searchbox"]/button').click()

# or
#driver.find_element(By.XPATH, "//*[@id='search_query_top' or @name=namme]").send_keys('T-shirts')

# and
#driver.find_element(By.XPATH, "//*[@id='search_query_top' and @name=namme]").send_keys('T-shirts')

# contains() - при динамическом изменении элементов сайта в зависимости от состояния
# //*[@id='start'] vs //*[@id='stop']
# //*[contains(@id,st)]
# а можно и так  ======>   //*[@id='start' or @id='stop')]
#driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys('T-shirts')

# starts-with() - начинается с 'st'
#driver.find_element(By.XPATH, "//button[starts-with(@name, 'submit_')]").click()

# текстовый метод
driver.find_element(By.XPATH, "//a[text()='Women']").click()












