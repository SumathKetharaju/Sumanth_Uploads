from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Sample test case started")

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://www.amazon.in/")

print(f"Title of the page is --> {driver.title}")

time.sleep(2)

search_bar = driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
print(f"search_bar.is_displayed() --> {search_bar.is_displayed()}")
search_bar.send_keys("Top 10 Sand disk Pendrives under 1000")
print(f"Entered value is --> {search_bar.get_attribute('value')}")
print(f"Title of the page after sending keys is --> {driver.title}")
time.sleep(2)
print("---------------------------------------------------------------------------------------")

search_button = driver.find_element(By.CSS_SELECTOR, "input[id='nav-search-submit-button']")
print(f"search_button.is_displayed() --> {search_button.is_displayed()}")
search_button.click()
print(f"Title of the page after click on search button is --> {driver.title}")
time.sleep(2)
print("---------------------------------------------------------------------------------------")

sand_disk_all_data = driver.find_element(By.CLASS_NAME, "sg-col-inner")
print(f"sand_disk_all_data.is_displayed() --> {sand_disk_all_data.is_displayed()}")
print(sand_disk_all_data.text)
print(f"Title of the page after entering the sand_disk_all_data text is --> {driver.title}")
time.sleep(2)
print("---------------------------------------------------------------------------------------")

sand_disk_32_gb = driver.find_element(By.LINK_TEXT, "SanDisk Cruzer Blade 32GB USB Flash Drive")
print(f"sand_disk_32_gb.is_displayed() --> {sand_disk_32_gb.is_displayed()}")
sand_disk_32_gb.click()
print(f"Title of the page after click on sand_disk_32_gb is --> {driver.title}")
time.sleep(2)
print("---------------------------------------------------------------------------------------")


sand_disk_32_gb_review = driver.find_element(By.CLASS_NAME, "a-size-base")
print(f"sand_disk_32_gb_review.is_displayed() --> {sand_disk_32_gb_review.is_displayed()}")
print(sand_disk_32_gb_review.text)
print(f"Title of the page after getting text of sand_disk_32_gb_review is --> {driver.title}")
time.sleep(5)
print("---------------------------------------------------------------------------------------")

driver.save_screenshot(r"C:\Users\SUMANTH\Desktop\Automation_Purposes\Automations\san_disk_32gb_pendrive_2.png")

driver.quit()

