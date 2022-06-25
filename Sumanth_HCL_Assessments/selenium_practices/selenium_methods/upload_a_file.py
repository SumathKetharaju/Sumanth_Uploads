from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
print(f"Title of the page is --> {driver.title}")

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

upload_file = driver.find_element(By.XPATH, '//*[@id="RESULT_FileUpload-10"]')
print(upload_file.is_displayed())
