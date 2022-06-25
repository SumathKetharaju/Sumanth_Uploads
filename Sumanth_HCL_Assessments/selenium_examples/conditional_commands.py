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

print("---------------------------------- After Giving email_address XPATH -------------------------------------------")

print(f"email_address.is_displayed() --> {email_address.is_displayed()}")
print(f"email_address.is_enabled() --> {email_address.is_enabled()}")

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

time.sleep(2)

password = local_driver.find_element(By.XPATH, "//*[@id='pass']")

print("---------------------------------- After Giving password XPATH-------------------------------------------")
print(f"password.is_displayed() --> {password.is_displayed()}")
print(f"password.is_enabled() --> {password.is_enabled()}")

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

time.sleep(2)

login = local_driver.find_element(By.XPATH, "//*[text()='Log In']")
print("---------------------------------- After Giving login XPATH-------------------------------------------")
print(f"login.is_displayed() --> {login.is_displayed()}")
print(f"login.is_enabled() --> {login.is_enabled()}")

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

time.sleep(5)

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")
print("Sample test case successfully completed")


print("---------------------------------- After checking XPATH of gmail-------------------------------------------")

time.sleep(2)

email_address.send_keys("sumanth@gmail.com")

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

time.sleep(2)

print("---------------------------------- After checking XPATH of password-------------------------------------------")

password.send_keys("sumanth123")

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

time.sleep(2)

print("---------------------------------- After checking XPATH of login-------------------------------------------")

login.click()

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

time.sleep(5)

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")

print("-------------------------------------------------------------------------------------")
print("Sample test case successfully completed")
print("-------------------------------------------------------------------------------------")

local_driver.close()

# local_driver.close()

