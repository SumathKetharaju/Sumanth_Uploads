from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Sample test case started")

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(15)

driver.get("https://www.amazon.in/")
print(f"Title of the page is --> {driver.title}")


amazon_pay = driver.find_element(By.LINK_TEXT, "Amazon Pay")
print(f"amazon_pay.is_displayed() --> {amazon_pay.is_displayed()}")
amazon_pay.click()
print(f"Title of the page is --> {driver.title}")
# time.sleep(2)
print("---------------------------------------------------------------------------------------")


pay_options = driver.find_elements(By.CLASS_NAME, "image-footer-text-desktop")
# print(f"landscape.is_displayed() --> {landscape.is_displayed()}")
# print(landscape)
print(len(pay_options))
for data in pay_options:
    print(data.text)
print(f"Title of the page is --> {driver.title}")
# time.sleep(2)
print("---------------------------------------------------------------------------------------")

# time.sleep(2)

# landscape = driver.find_element(By.CLASS_NAME, "landscape-image")
# print(f"landscape.is_displayed() --> {landscape.is_displayed()}")
# landscape.click()
# print(f"Title of the page is --> {driver.title}")
# # time.sleep(2)
# print("---------------------------------------------------------------------------------------")

# landscape = driver.find_elements(By.CLASS_NAME, "landscape-image")
# # print(f"landscape.is_displayed() --> {landscape.is_displayed()}")
# # print(landscape)
# print(len(landscape))
# # for data in landscape:
# #     print(data.text)
# print(f"Title of the page is --> {driver.title}")
# # time.sleep(2)
# print("---------------------------------------------------------------------------------------")

# search_button = driver.find_element(By.CSS_SELECTOR, "input[id='nav-search-submit-button']")
# print(f"search_button.is_displayed() --> {search_button.is_displayed()}")
# search_button.click()
# print(f"Title of the page is --> {driver.title}")
# # time.sleep(2)
# print("---------------------------------------------------------------------------------------")
#
# sand_disk_all_data = driver.find_element(By.CLASS_NAME, "sg-col-inner")
# print(f"sand_disk_all_data.is_displayed() --> {sand_disk_all_data.is_displayed()}")
# print(sand_disk_all_data.text)
# print(f"Title of the page is --> {driver.title}")
# # time.sleep(2)
# print("---------------------------------------------------------------------------------------")
