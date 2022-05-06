# explicit - явный, основан на состоянии ожидаемого элемента

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)
#mywait=WebDriverWait(driver, 10) # явное объявления ожидания

# если нужно игнорировать исключения и продолжать дальше
# poll_frequency = 2 -будет 5 раз по 2 секунды делать попытки вытянуть элемент
mywait=WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     Exception]
                     )

driver.get("https://google.com")
driver.maximize_window()

searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys('Selenium')
searchbox.submit()
searchlink=mywait.until(EC.visibility_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()



driver.quit()
