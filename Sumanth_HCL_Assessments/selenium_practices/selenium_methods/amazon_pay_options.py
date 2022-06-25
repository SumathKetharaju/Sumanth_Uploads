from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

print("Sample test case started")

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(15)

driver.get("https://www.amazon.in/")
print(f"Title of the page is --> {driver.title}")


amazon_pay = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Amazon Pay")))
print(f"amazon_pay.is_displayed() --> {amazon_pay.is_displayed()}")
amazon_pay.click()
print(f"Title of the page is --> {driver.title}")
# time.sleep(2)
print("---------------------------------------------------------------------------------------")

# selenium.webdriver.support.expected_conditions.presence_of_all_elements_located(locator) --> An expectation for
# checking that there is at least one element present on a web page. locator is used to find the element returns the
# list of WebElements once they are located
pay_options = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "image-footer-text-desktop")))
# print(f"landscape.is_displayed() --> {landscape.is_displayed()}")
# print(landscape)
print(len(pay_options))
for data in pay_options:
    print(data.text)
print(f"Title of the page is --> {driver.title}")
# time.sleep(2)
print("---------------------------------------------------------------------------------------")