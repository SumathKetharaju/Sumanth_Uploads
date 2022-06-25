import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Sample test case started")

local_driver = webdriver.Chrome()

local_driver.maximize_window()

local_driver.get("https://www.facebook.com/")

print("--------------------------------------- Pinged Facebook ---------------------------------------------------")
print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

time.sleep(2)

email_address = local_driver.find_element(By.XPATH, "//*[@id='email']")
email_address.send_keys("xxxxxx@gmail.com")

print("---------------------------------- After Giving email_address XPATH-------------------------------------------")
print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

time.sleep(2)

password = local_driver.find_element(By.XPATH, "//*[@id='pass']")
password.send_keys("xxxxxxx")

print("-------------------------------------- After Giving password XPATH-------------------------------------------")
print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

time.sleep(2)

login = local_driver.find_element(By.XPATH, "//*[text()='Log In']")
login.click()

print("-------------------------------------- After Giving logging XPATH-------------------------------------------")
print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

time.sleep(5)

print("-------------------------------------- After Giving all locators -------------------------------------------")
print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

print("-------------------------------------------------------------------------------------------------------------")
print("Sample test case successfully completed")

# local_driver.close()

