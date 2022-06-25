from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.programiz.com/python-programming")

file_handling = driver.find_element(By.XPATH, "/html/body/main/div[7]/div/div/div/div/div[1]/div[1]/div/ul/li[5]/a")

action = ActionChains(driver)
time.sleep(2)

action.move_to_element(file_handling)
time.sleep(2)

action.click()
time.sleep(2)

exception_handling = driver.find_element(By.CSS_SELECTOR, 'a[title="Python Errors and Built-in Exceptions"]')
print(f"exception_handling.is_displayed() --> {exception_handling.is_displayed()}")
action.move_to_element(exception_handling)
time.sleep(2)

action.click()

action.perform()

driver.save_screenshot(r"C:\Users\SUMANTH\Desktop\Automation_Purposes\Automations\sample_image_2.png")




