from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
print(f"Title of the page is --> {driver.title}")

driver.get("https://smallpdf.com/blog/sample-pdf")
time.sleep(2)

download = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/article/div[7]/a/div/span')
print(f"download.is_displayed() --> {download.is_displayed()}")
download.click()
