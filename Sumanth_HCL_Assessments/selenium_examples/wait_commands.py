from selenium import webdriver
from selenium.webdriver.common.by import By

print("Sample test case started")

local_driver = webdriver.Chrome()

local_driver.maximize_window()

local_driver.get("https://www.facebook.com/")

local_driver.implicitly_wait(2)

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

local_driver.implicitly_wait(2)

email_address = local_driver.find_element(By.XPATH, "//*[@id='email']")
email_address.send_keys("sumanth@gmail.com")

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

local_driver.implicitly_wait(2)

password = local_driver.find_element(By.XPATH, "//*[@id='pass']")
password.send_keys("sumanth123")

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

local_driver.implicitly_wait(2)

login = local_driver.find_element(By.XPATH, "//*[text()='Log In']")
login.click()

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

print("Sample test case successfully completed")

local_driver.close()

