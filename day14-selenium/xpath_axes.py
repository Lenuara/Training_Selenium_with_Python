from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("/Users/admin/PycharmProjects/drivers/chromedriver")
driver=webdriver.Chrome(service=serv)
driver.get('http://money.rediff.com/gainers/bse/daily/groupa/')
#driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

#self
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/self::a" ).text
# print(text_msg) # India Tourism De

#parent
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/parent::td").text
# print(text_msg) # India Tourism De

# child
# childs=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/child::td")
# print(len(childs))

#ancestor
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr").text
# print(text_msg)

#descendant
#descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/descendant::*")
#print(len(descendants)) #7

# following
# followings=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/following::*")
# print(len(followings)) #242

# following-sibling
# followings_sibling=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/following-sibling::*")
# print(len(followings_sibling)) #13

# preceding
# precedings=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/preceding::tr")
# print(len(precedings)) #188

# preceding-sibling
precedings_sibling=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/preceding-sibling::*")
print(len(precedings_sibling)) #187






driver.close()

