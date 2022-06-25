from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
print(f"Title of the page is --> {driver.title}")

driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(2)

username = driver.find_element(By.XPATH, "//*[@id='txtUsername']")
username.send_keys("Admin")
time.sleep(2)
print(f"Entered Username is {username.get_attribute('value')}")
print(f"Title of the page is --> {driver.title}")

password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password.send_keys("admin123")
time.sleep(2)
print(f"Entered Username is {password.get_attribute('value')}")
print(f"Title of the page is --> {driver.title}")

login_option = driver.find_element(By.XPATH, "//*[@id='btnLogin']")
login_option.click()
time.sleep(2)
print(f"Title of the page is --> {driver.title}")

admin = driver.find_element(By.ID, 'menu_admin_viewAdminModule')
user_management = driver.find_element(By.ID, 'menu_admin_UserManagement')
users = driver.find_element(By.ID, 'menu_admin_viewSystemUsers')

mouse_hover_action = ActionChains(driver)
# mouse_hover_action.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()

mouse_hover_action.move_to_element(admin)
mouse_hover_action.move_to_element(user_management)
mouse_hover_action.move_to_element(users)
mouse_hover_action.click()
mouse_hover_action.perform()


# driver.get("https://www.tutorialspoint.com/about/about_careers.htm")  # identify element
#
# driver.maximize_window()
# time.sleep(3)
# print('Page title: ' + driver.title)
#
# s = driver.find_element(By.LINK_TEXT, "Privacy Policy")  # instance of ActionChains
#
# a = ActionChains(driver)  # move to element
# time.sleep(3)
# print('Page title: ' + driver.title)
#
# a.move_to_element(s)  # click
# time.sleep(3)
# print('Page title: ' + driver.title)
#
# a.click().perform()  # get page title
# time.sleep(3)
# print('Page title: ' + driver.title)
#
# print('Page title: ' + driver.title)  # driver quit

driver.close()


