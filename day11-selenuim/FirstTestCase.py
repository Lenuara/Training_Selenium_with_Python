from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By

s=Service("/Users/admin/PycharmProjects/drivers/chromedriver")

driver = webdriver.Chrome(service=s)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME, value="txtUsername").clear()
driver.find_element(By.NAME, value="txtUsername").send_keys("Admin")
driver.find_element(By.ID, value="txtPassword").clear()
driver.find_element(By.ID, value="txtPassword").send_keys("admin123")
driver.find_element(By.ID, value="btnLogin").click()
driver.find_element(By.XPATH, "")

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()