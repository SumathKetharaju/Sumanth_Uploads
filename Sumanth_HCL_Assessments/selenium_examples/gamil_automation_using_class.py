from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

print("Gmail Test case started")

driver = webdriver.Chrome()

driver.maximize_window()

driver.delete_all_cookies()

driver.get("https://mail.google.com/")

# DeprecationWarning: find_elements_by_* commands are deprecated. Please use find_elements()
# driver.find_elements_by_class_name("bcAAsb")  #not a valid one

# AttributeError: 'list' object has no attribute 'click'
# driver.find_elements(By.CLASS_NAME, "bcAAsb").click()  #not a valid one

# AttributeError: 'list' object has no attribute 'click'
# gmail_id = driver.find_elements(By.CLASS_NAME, "bcAAsb").click()  #not a valid one

gmail_id = driver.find_elements(By.CLASS_NAME, "bcAAsb")
# gmail_id = driver.find_elements(By.CLASS_NAME, "bcAAsb")[0].send_keys("Sumanth")
# gmail_id.click()
# gmail_id.send_keys("sumanth")

print(driver.title)
print("Gmail Test case successfully completed")