import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# print(selenium.__version__)
print("Gmail Test case started")

driver = webdriver.Chrome()

driver.maximize_window()

driver.delete_all_cookies()

driver.get("https://mail.google.com/")

driver.find_element_by_xpath("//body[@id='yDmH0d']").send_keys("sumanth") #not a valid one

# driver.find_elements(By.ID, "yDmH0d").click()  #not a valid one

# gmail_id = driver.find_elements(By.ID, "yDmH0d").click()  #not a valid one

# gmail_id = driver.find_elements(By.ID, "yDmH0d")[0]
# gmail_id.click()
# gmail_id.send_keys("sumanth")

print("Gmail Test case successfully completed")

