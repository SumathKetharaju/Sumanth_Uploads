import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Sample test case started")

local_driver = webdriver.Chrome()

local_driver.maximize_window()

local_driver.get("https://www.programiz.com/python-programming")

print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")
time.sleep(2)

local_driver.get("https://www.programiz.com/python-programming/first-program")
print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")
time.sleep(2)

local_driver.back()
print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")
time.sleep(2)

local_driver.forward()
print(f"Current Page is {local_driver.title}")
print(f"Current URL is {local_driver.current_url}")
time.sleep(2)
print("Sample test case successfully completed")

# local_driver.close()  # closes current browser only
# local_driver.quit()   # close all browsers
