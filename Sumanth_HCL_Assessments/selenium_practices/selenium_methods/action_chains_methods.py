from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
# time.sleep(2)
print(f"Tile of the page is --> {driver.title}")

driver.get("https://www.programiz.com/python-programming")
time.sleep(2)
print(f"Tile of the page is --> {driver.title}")

functions = driver.find_element(By.XPATH, "/html/body/main/div[7]/div/div/div/div/div[1]/div[1]/div/ul/li[3]/a")
# python_global_keyword = driver.find_element(By.XPATH, "//*[@id='functions']/div/div/ul/li[6]/a")
python_global_keyword = driver.find_element(By.XPATH, "/html/body/main/div[7]/div/div/div/div/div[2]/div[5]/div/div/ul/li[5]/a")

action = ActionChains(driver)

action.move_to_element(functions)
time.sleep(2)
print(f"functions --> {functions.text}")

print(driver.title)

action.click()
time.sleep(2)

# action.click_and_hold(python_global_keyword)
# time.sleep(2)

action.click(python_global_keyword)
time.sleep(5)
print(f"python_global_keyword --> {python_global_keyword.text}")
print(driver.title)
# action.pause(5)
# action.click(python_global_keyword)
# action.release(python_global_keyword)
# action.reset_actions()
# action.release(python_global_keyword)
# advertisement = driver.find_element(By.CSS_SELECTOR, 'svg[viewBox="0 0 48 48"]')
# action.click(advertisement)

# action.move_by_offset(200, 200)

action.perform()



