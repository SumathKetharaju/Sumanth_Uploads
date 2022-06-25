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


# selenium.webdriver.support.expected_conditions.presence_of_element_located(locator) --> An expectation for checking
# that an element is present on the DOM of a page. This does not necessarily mean that the element is visible. locator -
# used to find the element returns the WebElement once it is located.

search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#twotabsearchtextbox")))
print(search_bar)
print(EC.presence_of_element_located((By.CSS_SELECTOR, "input#twotabsearchtextbox")))
print(f"search_bar.is_displayed() --> {search_bar.is_displayed()}")
search_bar.send_keys("Top 10 Sand disk Pendrives under 1000")
print(f"Entered value is --> {search_bar.get_attribute('value')}")
print(f"Title of the page is --> {driver.title}")

print("---------------------------------------------------------------------------------------")

# selenium.webdriver.support.expected_conditions.element_to_be_clickable(mark) --> An Expectation for checking an
# element is visible and enabled such that you can click it. element is either a locator (text) or an WebElement
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='nav-search-submit-button']")))
print(f"search_button.is_displayed() --> {search_button.is_displayed()}")
search_button.click()
print(f"Title of the page is --> {driver.title}")

print("---------------------------------------------------------------------------------------")
#
sand_disk_all_data = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "sg-col-inner")))
print(f"sand_disk_all_data.is_displayed() --> {sand_disk_all_data.is_displayed()}")
print(sand_disk_all_data.text)
print(f"Title of the page is --> {driver.title}")

print("---------------------------------------------------------------------------------------")

sand_disk_32_gb = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "SanDisk Cruzer Blade 32GB USB Flash Drive")))
print(f"sand_disk_32_gb.is_displayed() --> {sand_disk_32_gb.is_displayed()}")
sand_disk_32_gb.click()
print(f"Title of the page is --> {driver.title}")

print("---------------------------------------------------------------------------------------")


sand_disk_32_gb_review = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "a-size-base")))
print(f"sand_disk_32_gb_review.is_displayed() --> {sand_disk_32_gb_review.is_displayed()}")
print(sand_disk_32_gb_review.text)
print(f"Title of the page is --> {driver.title}")
# time.sleep(2)
print("---------------------------------------------------------------------------------------")

# sand_disk_32_gb_cost = driver.find_element(By.XPATH, "//*[test()=369]")
# print(f"sand_disk_32_gb_cost.is_displayed() --> {sand_disk_32_gb_cost.is_displayed()}")
# sand_disk_32_gb_cost.click()
# print(f"Title of the page is --> {driver.title}")
# time.sleep(2)


driver.quit()
