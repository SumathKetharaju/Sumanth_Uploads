import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Sample test case started")

local_driver = webdriver.Chrome()

local_driver.maximize_window()

local_driver.get("http://www.africau.edu/images/default/sample.pdf")

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")
time.sleep(2)

chrome_driver_version = local_driver.find_element(By.XPATH, '//*[@id="icon"]')
chrome_driver_version.is_displayed()
print(f"chrome_driver_version.is_displayed() --> {chrome_driver_version.is_displayed()}")
chrome_driver_version.click()
time.sleep(2)
#
# print(f"Current Page is --> {local_driver.title}")
# print(f"Current URL is --> {local_driver.current_url}")
#
# # windows_chrome_driver = local_driver.find_element(By.XPATH, '/html/body/table/tbody/tr[7]/td[2]/a')
# # print(f"windows_chrome_driver.is_displayed() --> {windows_chrome_driver.is_displayed()}")
# # windows_chrome_driver.click()
#
# # time.sleep(2)
# # print(f"Current Page is --> {local_driver.title}")
# # print(f"Current URL is --> {local_driver.current_url}")

local_driver.quit()


