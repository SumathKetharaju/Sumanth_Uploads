from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# It opens the browser
driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.programiz.com/python-programming")


object_and_class = driver.find_element(By.LINK_TEXT, "Object & Class")
print(f"search_bar_using_tag_name.is_displayed() --> {object_and_class.is_displayed()}")
object_and_class.click()
print(object_and_class.text)
time.sleep(2)

print(f"Title of the page is --> {driver.title}")

oops_concept = driver.find_element(By.XPATH, "//*[@id='object-class']/div/div/ul/li[1]/a")
print(f"oops_concept.is_displayed() --> {oops_concept.is_displayed()}")
oops_concept.click()
print(oops_concept.text)

# uniccmp

# oops = driver.find_element(By.ID, "uniccmp")
# print(f"oops.is_displayed() --> {oops.is_displayed()}")
# # oops_concept.click()
# print(oops.text)
# time.sleep(5)

print(f"Title of the page is --> {driver.title}")

# driver.close()


"""
# It opens the browser
# driver = webdriver.Chrome()
#
# driver.maximize_window()
#
# driver.get("https://www.programiz.com/python-programming")


# search_bar_using_tag_name = driver.find_element(By.TAG_NAME, "input")
# print(f"search_bar_using_tag_name.is_displayed() --> {search_bar_using_tag_name.is_displayed()}")
# search_bar_using_tag_name.send_keys("https://www.facebook.com")
# time.sleep(2)
#
# print(f"Title of the page is --> {driver.title}")
#
#
# search_button_using_tag_name = driver.find_element(By.CLASS_NAME, "match")
# print(f"search_bar_using_tag_name.is_displayed() --> {search_button_using_tag_name.is_displayed()}")
# search_button_using_tag_name.click()
#
# print(f"Title of the page is --> {driver.title}")
# print(f"Title of the page is --> {search_bar_using_tag_name.get_attribute('value')}")
# driver.close()

# "------------------------------------------------------------------------------------------------------------"
"""