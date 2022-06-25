from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Sample test case started")

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.shoppersstop.com/")
print(f"Title of the page is --> {driver.title}")
time.sleep(2)

gifts = driver.find_element(By.LINK_TEXT, "GIFTS")
print(f"Title of the page is --> {driver.title}")
print(f"Gifts.is_displayed() --> {gifts.is_displayed()}")
gifts.click()
print(f"Title of the page is --> {driver.title}")

titan_belts = driver.find_element(By.XPATH, "/html/body/main/div[19]/section/div[2]/div[6]/a/img")
print(f"Title of the page is --> {driver.title}")
print(f"Titan_belts.is_displayed() --> {titan_belts.is_displayed()}")
titan_belts.click()
print(f"Title of the page is --> {driver.title}")

# brown

brown_color_belts = driver.find_element(By.CSS_SELECTOR, "input[id='brown']")
print(f"Title of the page is --> {driver.title}")
check = brown_color_belts.is_displayed()
print(f"brown_color_belts.is_displayed() --> {check}")
if check:
    brown_color_belts.click()
    print(f"Title of the page is --> {driver.title}")

# cross_belts = driver.find_element(By.XPATH, "//*[@id='tab5']/div[2]/div/div/ul/li[2]/form/div/label")
# print(f"Title of the page is --> {driver.title}")
# print(f"cross_belts.is_displayed() --> {cross_belts.is_displayed()}")
# cross_belts.click()
# print(f"Title of the page is --> {driver.title}")

# cross_belt = driver.find_element(By.XPATH, "//*[@id='primaryImage']")
# print(f"Title of the page is --> {driver.title}")
# print(f"cross_belt.is_displayed() --> {cross_belt.is_displayed()}")
# cross_belt.click()
# print(f"Title of the page is --> {driver.title}")
# print(len(check_boxes))
# search_bar = driver.find_element(By.ID, "js-site-search-input")
# print(f"search_bar.is_displayed() --> {search_bar.is_displayed()}")
# search_bar.send_keys("men shirts")
# print(f"Entered value is --> {search_bar.get_attribute('value')}")
# time.sleep(2)

# search_button = driver.find_element(By.CSS_SELECTOR, "input.btnsearch")
# print(f"search_button.is_displayed() --> {search_button.is_displayed()}")
# search_button.click()
