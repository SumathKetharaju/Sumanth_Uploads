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

source_element = driver.find_element(By.XPATH, "//*[@id='draggable']/p")
target_element = driver.find_element(By.XPATH, "//*[@id='droppable']")
time.sleep(2)
print(f"Title of the page is --> {driver.title}")

action = ActionChains(driver)
# mouse_hover_action.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()

action.drag_and_drop(source_element, target_element).perform()

