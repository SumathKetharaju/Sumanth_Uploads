# /html/body/main/div[5]
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# It opens the browser
driver = webdriver.Chrome()

driver.maximize_window()

# Target URL
driver.get("https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")

# print(driver.title)

# Printing the whole body text
print(driver.find_element(By.XPATH, "/html/body").text)

# Closing the driver
# driver.close()

# driver.get("https://www.programiz.com/python-programming")
#
#
# python_info = driver.find_element(By.XPATH, "/html/body/main/div[5]")
# print(f"python_info.is_displayed() --> {python_info.is_displayed()}")
# # python_info.click()
# print(python_info.text)
# time.sleep(2)

# print(f"Title of the page is --> {driver.title}")
#
# oops_concept = driver.find_element(By.XPATH, "//*[@id='object-class']/div/div/ul/li[1]/a")
# print(f"oops_concept.is_displayed() --> {oops_concept.is_displayed()}")
# oops_concept.click()
# print(oops_concept.text)
# time.sleep(5)

# print(f"Title of the page is --> {driver.title}")
