from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.jotform.com/build/220749245628462")
print(f"Title of the page is --> {driver.title}")

input_boxes = driver.find_elements(By.XPATH, "//input[@type='text']")
# print(check_boxes)
print(f"Available check boxes are --> {len(input_boxes)}")
print(f"Current Page is --> {driver.title}")
print(f"Current URL is --> {driver.current_url}")

first_name = driver.find_element(By.NAME, 'q3_fullName3[first]')
first_name.is_displayed()
print(f"first_name.is_displayed() --> {first_name.is_displayed()}")
first_name.send_keys("Ramesh")
print(f"The entered value is --> {first_name.get_attribute('value')}")
time.sleep(2)

last_name = driver.find_element(By.NAME, 'q3_fullName3[last]')
last_name.is_displayed()
print(f"first_name.is_displayed() --> {last_name.is_displayed()}")
last_name.send_keys("Kumar")
print(f"The entered value is --> {last_name.get_attribute('value')}")
time.sleep(2)

gmail = driver.find_element(By.NAME, "q4_email4")
gmail.is_displayed()
print(f"gmail.is_displayed() --> {gmail.is_displayed()}")
gmail.send_keys("rameshkumar000@gmail.com")
print(f"The entered value is --> {gmail.get_attribute('value')}")
time.sleep(2)
#
street_address_1 = driver.find_element(By.NAME, "q9_address9[addr_line1]")
street_address_1.is_displayed()
print(f"street_address_1.is_displayed() --> {street_address_1.is_displayed()}")
street_address_1.send_keys("Sri ram Nagar")
print(f"The entered value is --> {street_address_1.get_attribute('value')}")
time.sleep(2)
#
street_address_2 = driver.find_element(By.NAME, "q9_address9[addr_line2]")
street_address_2.is_displayed()
print(f"street_address_2.is_displayed() --> {street_address_2.is_displayed()}")
street_address_2.send_keys("Opposite to vijaya mahal")
print(f"The entered value is --> {street_address_2.get_attribute('value')}")
time.sleep(2)

city = driver.find_element(By.NAME, "q9_address9[city]")
city.is_displayed()
print(f"city.is_displayed() --> {city.is_displayed()}")
city.send_keys("Kurnool")
print(f"The entered value is --> {city.get_attribute('value')}")
time.sleep(2)

state = driver.find_element(By.NAME, "q9_address9[state]")
state.is_displayed()
print(f"state.is_displayed() --> {state.is_displayed()}")
state.send_keys("Tamil nadu")
print(f"The entered value is --> {state.get_attribute('value')}")
time.sleep(2)

postal_code = driver.find_element(By.NAME, "q9_address9[postal]")
postal_code.is_displayed()
print(f"postal_code.is_displayed() --> {postal_code.is_displayed()}")
postal_code.send_keys("568421")
print(f"The entered value is --> {postal_code.get_attribute('value')}")
time.sleep(2)

drop_down = driver.find_element(By.NAME, "q9_address9[country]")
drop_down.is_displayed()
print(f"drop_down.is_displayed() --> {drop_down.is_displayed()}")

drop_down_selection = Select(drop_down)
print(f"Total dropdown selection options are --> {len(drop_down_selection.options)}")
drop_down_selection.select_by_visible_text("India")

area_code = driver.find_element(By.NAME, "q5_phoneNumber5[area]")
area_code.is_displayed()
print(f"area_code.is_displayed() --> {area_code.is_displayed()}")
area_code.send_keys("+91")
print(f"The entered value is --> {area_code.get_attribute('value')}")
time.sleep(2)


phone_number = driver.find_element(By.NAME, "q5_phoneNumber5[phone]")
phone_number.is_displayed()
print(f"phone_number.is_displayed() --> {phone_number.is_displayed()}")
phone_number.send_keys("8580369581")
print(f"The entered value is --> {phone_number.get_attribute('value')}")
time.sleep(2)

# age_above_18 = driver.find_element(By.NAME, "form-radio validate[required] form-validation-error")
# age_above_18.is_displayed()
# print(f"age_above_18.is_displayed() --> {age_above_18.is_displayed()}")
# age_above_18.click()
# # print(f"The entered value is --> {postal_code.get_attribute('value')}")
# time.sleep(1)

where_did_you_here = driver.find_element(By.CSS_SELECTOR, "input[name='q16_whereDid']")
where_did_you_here.is_displayed()
print(f"where_did_you_here.is_displayed() --> {where_did_you_here.is_displayed()}")
where_did_you_here.send_keys("I am here from particular website")
print(f"The entered value is --> {postal_code.get_attribute('value')}")
time.sleep(2)

company = driver.find_element(By.NAME, "q13_companygrouporganization13")
company.is_displayed()
print(f"company.is_displayed() --> {company.is_displayed()}")
company.send_keys("Jira")
print(f"The entered value is --> {company.get_attribute('value')}")
time.sleep(2)

how_many_members = driver.find_element(By.NAME, "q14_howMembers14")
how_many_members.is_displayed()
print(f"how_many_members.is_displayed() --> {how_many_members.is_displayed()}")
how_many_members.send_keys("5")
print(f"The entered value is --> {how_many_members.get_attribute('value')}")
time.sleep(2)

driver.quit()

# drop_down = driver.find_element(By.NAME, "q9_address9[country]")
# drop_down.is_displayed()
# print(f"drop_down.is_displayed() --> {drop_down.is_displayed()}")
#
# drop_down_selection = Select(drop_down)
#
# print(f"Total dropdown selection options are --> {len(drop_down_selection.options)}")
#
# drop_down_selection.select_by_visible_text("India")
# # print(f"Selected options is --> {len(drop_down_selection.all_selected_options)}")
#
# drop_down_selection.select_by_value("Algeria")
# # print(f"Selected options is --> {len(drop_down_selection.all_selected_options)}")
#
# drop_down_selection.select_by_index(6)
# # print(f"Selected options is --> {len(drop_down_selection.all_selected_options)}")
#
# print(type(drop_down_selection))
# for option in drop_down_selection.options:
#     print(option.text)


# print(len(drop_down))
# drop_down.send_keys("Nellore")
# print(f"The entered value is --> {drop_down.get_attribute('value')}")
# time.sleep(1)



#
# print(f"Current Page is --> {driver.title}")
# print(f"Current URL is --> {driver.current_url}")
#
# search_buttom = driver.find_element(By.ID, 'nav-search-submit-button')
# print(f"search_buttom.is_displayed() --> {search_buttom.is_displayed()}")
# search_buttom.click()
# print(f"Current Page is --> {driver.title}")
# print(f"Current URL is --> {driver.current_url}")
#
# # android_xpath = driver.find_element(By.XPATH, "//*[text()='Android']")
# # samsung_xpath = driver.find_element(By.XPATH, "//*[@id='p_89/Samsung']/span/a/div/label/i")

