from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import os

path_of_image = r"C://Users/SUMANTH/Desktop/Automation_Purposes/Automations/sample_image.jpg"
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
print(f"Title of the page is --> {driver.title}")

driver.get("https://www.ilovepdf.com/")
time.sleep(2)
print(f"Title of the page is --> {driver.title}")

jpg_to_pdf = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[12]/a/h3")
print(f"jpg_to_pdf.is_displayed() --> {jpg_to_pdf.is_displayed()}")
jpg_to_pdf.click()
time.sleep(2)
print(f"Title of the page is --> {driver.title}")

select_jpj_images = driver.find_element(By.LINK_TEXT, "Select JPG images")
print(f"select_jpj_images.is_displayed() --> {select_jpj_images.is_displayed()}")
select_jpj_images.send_keys(path_of_image)
time.sleep(2)
print(f"Current value is --> {select_jpj_images.get_attribute('value')}")
print(f"Title of the page is --> {driver.title}")


