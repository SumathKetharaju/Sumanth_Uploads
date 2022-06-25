from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html")
print(f"Title of the page is --> {driver.title}")

application_type_drop_down = driver.find_element(By.XPATH, '//*[@id="type"]')
application_type_drop_down_selection = Select(application_type_drop_down)
print(f"application_type_drop_down.is_displayed() --> {application_type_drop_down.is_displayed()}")
print(f"Total Number of Application dropdown options are --> {len(application_type_drop_down_selection.options)}")
print(f"--------------------------- Total Available Application dropdown options are ------------------------------ ")
for application_options in application_type_drop_down_selection.options:
    print(application_options.text)
print("--------------------------------------------------------------------------------")
application_type_drop_down_selection.select_by_index(2)
time.sleep(2)

category_drop_down = driver.find_element(By.XPATH, '//*[@id="cat_applicant1"]')
category_drop_down_selection = Select(category_drop_down)
print(f"category_drop_down.is_displayed() --> {category_drop_down.is_displayed()}")
print(f"Total Number of Category dropdown selection options are --> {len(category_drop_down_selection.options)}")
print(f"---------------------------- Total Available Category dropdown options are ----------------------------- ")
for category_options in category_drop_down_selection.options:
    print(category_options.text)
print("--------------------------------------------------------------------------------")
category_drop_down_selection.select_by_visible_text("INDIVIDUAL")
time.sleep(2)

titles_drop_down = driver.find_element(By.XPATH, '//*[@id="rvNameInitials"]')
titles_drop_down_selection = Select(titles_drop_down)
print(f"titles_drop_down.is_displayed() --> {titles_drop_down.is_displayed()}")
print(f"Total Number of Title dropdown selection options are --> {len(titles_drop_down_selection.options)}")
print(f"---------------------------- Total Available Title dropdown options are ----------------------------- ")
for title_options in titles_drop_down_selection.options:
    print(title_options.text)
print("--------------------------------------------------------------------------------")
titles_drop_down_selection.select_by_index(1)
time.sleep(2)

application_type_drop_down = driver.find_element(By.XPATH, '//*[@id="type"]')
application_type_drop_down_selection = Select(application_type_drop_down)
print(application_type_drop_down_selection.first_selected_option.text)

category_drop_down = driver.find_element(By.XPATH, '//*[@id="cat_applicant1"]')
category_drop_down_selection = Select(category_drop_down)
print(category_drop_down_selection.first_selected_option)

# titles_drop_down = driver.find_element(By.XPATH, '//*[@id="rvNameInitials"]')
# titles_drop_down_selection = Select(titles_drop_down)
# titles_drop_down_selection.deselect_by_index(1)
