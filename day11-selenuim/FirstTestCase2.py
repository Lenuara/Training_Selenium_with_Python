from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By

s=Service("/Users/admin/PycharmProjects/drivers/chromedriver")

driver = webdriver.Chrome(service=s)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.XPATH, value="//*[@id='Email']").clear()
driver.find_element(By.XPATH, value="//*[@id='Email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH, value="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input").clear()
driver.find_element(By.XPATH, value="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input").send_keys("admin")
driver.find_element(By.XPATH, value="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()


act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"

if act_title == exp_title:
     print("Login Test Passed")
else:
     print("Login Test Failed")

driver.close()