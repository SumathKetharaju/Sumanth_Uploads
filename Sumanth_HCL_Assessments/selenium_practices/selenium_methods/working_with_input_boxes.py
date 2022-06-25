from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.amazon.in/")
print(f"Title of the page is --> {driver.title}")

search_bar = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
search_bar.is_displayed()
print(f"search.is_displayed() --> {search_bar.is_displayed()}")
search_bar.send_keys("Top 10 mobiles in 2022")
# time.sleep(2)

print(f"Current Page is --> {driver.title}")
print(f"Current URL is --> {driver.current_url}")

search_button = driver.find_element(By.ID, 'nav-search-submit-button')
print(f"search_button.is_displayed() --> {search_button.is_displayed()}")
search_button.click()
print(f"Current Page is --> {driver.title}")
print(f"Current URL is --> {driver.current_url}")

# android_xpath = driver.find_element(By.XPATH, "//*[text()='Android']")
# samsung_xpath = driver.find_element(By.XPATH, "//*[@id='p_89/Samsung']/span/a/div/label/i")
check_boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# print(check_boxes)
print(f"Available check boxes are --> {len(check_boxes)}")
print(f"Current Page is --> {driver.title}")
print(f"Current URL is --> {driver.current_url}")





# for box in check_boxes:
#     pass
#     # print(f"box.is_displayed() --> {box.is_displayed()} and box.is_selected() --> {box.is_selected()}")
#
# # print(a-size-base a-color-base)
#
# class_name = driver.find_elements(By.CLASS_NAME, "a-size-base a-color-base")
# # print(f"class_name.is_displayed() --> {class_name.is_displayed()}")
# print(class_name)
# for data in class_name:
#     print(data.is_displayed())
#     print(data.text)


# from selenium import webdriver
#
# # browser exposes an executable file
# # Through Selenium test we will invoke the executable file which will then #invoke actual browser
# driver = webdriver.Chrome()
#
# # to maximize the browser window
# driver.maximize_window()
#
# # get method to launch the URL
# driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# # to refresh the browser
# driver.refresh()
# # identifying the checkboxes with type attribute in a list
# chk =driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# # len method is used to get the size of that list
# print(len(chk))
# #to close the browser
# # driver.close()
