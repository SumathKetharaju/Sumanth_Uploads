from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html")
time.sleep(2)
print(f"Title of the page is --> {driver.title}")
print(f"URL of the page is --> {driver.current_url}")

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

sur_name = driver.find_element(By.ID, 'l_name_end')
print(f"sur_name.is_displayed() --> {sur_name.is_displayed()}")
sur_name.send_keys("Bollineni")
print(f"The entered Sur name is --> {sur_name.get_attribute('value')}")
time.sleep(2)

first_name = driver.find_element(By.NAME, 'firstName')
print(f"first_name.is_displayed() --> {first_name.is_displayed()}")
first_name.send_keys("Raki")
print(f"The entered First name is --> {first_name.get_attribute('value')}")
time.sleep(2)

middle_name = driver.find_element(By.CSS_SELECTOR, 'input#m_name_end')
print(f"middle_name.is_displayed() --> {middle_name.is_displayed()}")
middle_name.send_keys("Kumar")
print(f"The entered Middle name is --> {middle_name.get_attribute('value')}")
time.sleep(2)

date_of_birth = driver.find_element(By.CSS_SELECTOR, 'input[id="date_of_birth_reg"]')
print(f"date_of_birth.is_displayed() --> {date_of_birth.is_displayed()}")
date_of_birth.send_keys("12/06/1998")
print(f"The entered Date of Birth is --> {date_of_birth.get_attribute('value')}")
time.sleep(2)

email_id = driver.find_element(By.ID, 'email_id2')
print(f"email_id.is_displayed() --> {date_of_birth.is_displayed()}")
email_id.send_keys("bollineniuraki@gmail.com")
print(f"The entered EmailId is --> {email_id.get_attribute('value')}")
time.sleep(2)

mobile_number = driver.find_element(By.XPATH, '//*[@id="rvContactNo"]')
print(f"mobile_number.is_displayed() --> {date_of_birth.is_displayed()}")
mobile_number.send_keys("9532684172")
print(f"The entered Mobile Number is --> {mobile_number.get_attribute('value')}")
time.sleep(2)

# driver.quit()













# application_type_drop_down = driver.find_element(By.XPATH, '//*[@id="select2-type-container"]')
# print(f"application_type_drop_down.is_displayed() --> {application_type_drop_down.is_displayed()}")
# # application_type_drop_down.click()
# #
# indian_citizen = driver.find_element(By.XPATH, '//*[@id="type"]/option[2]')
# print(f"indian_citizen.is_displayed() --> {indian_citizen.is_displayed()}")
# indian_citizen.click()
# # print(check_boxes)
# print(f"Available check boxes are --> {len(input_boxes)}")
# print(f"Current Page is --> {driver.title}")
# print(f"Current URL is --> {driver.current_url}")
#
# first_name = driver.find_element(By.NAME, 'q3_fullName3[first]')
# first_name.is_displayed()
# print(f"first_name.is_displayed() --> {first_name.is_displayed()}")
# first_name.send_keys("Ramesh")
# print(f"The entered value is --> {first_name.get_attribute('value')}")
# time.sleep(2)
#
# last_name = driver.find_element(By.NAME, 'q3_fullName3[last]')
# last_name.is_displayed()
# print(f"first_name.is_displayed() --> {last_name.is_displayed()}")
# last_name.send_keys("Kumar")
# print(f"The entered value is --> {last_name.get_attribute('value')}")
# time.sleep(2)
#
# gmail = driver.find_element(By.NAME, "q4_email4")
# gmail.is_displayed()
# print(f"gmail.is_displayed() --> {gmail.is_displayed()}")
# gmail.send_keys("rameshkumar000@gmail.com")
# print(f"The entered value is --> {gmail.get_attribute('value')}")
# time.sleep(2)
# #
# street_address_1 = driver.find_element(By.NAME, "q9_address9[addr_line1]")
# street_address_1.is_displayed()
# print(f"street_address_1.is_displayed() --> {street_address_1.is_displayed()}")
# street_address_1.send_keys("Sri ram Nagar")
# print(f"The entered value is --> {street_address_1.get_attribute('value')}")
# time.sleep(2)
# #
# street_address_2 = driver.find_element(By.NAME, "q9_address9[addr_line2]")
# street_address_2.is_displayed()
# print(f"street_address_2.is_displayed() --> {street_address_2.is_displayed()}")
# street_address_2.send_keys("Opposite to vijaya mahal")
# print(f"The entered value is --> {street_address_2.get_attribute('value')}")
# time.sleep(2)
#
# city = driver.find_element(By.NAME, "q9_address9[city]")
# city.is_displayed()
# print(f"city.is_displayed() --> {city.is_displayed()}")
# city.send_keys("Kurnool")
# print(f"The entered value is --> {city.get_attribute('value')}")
# time.sleep(2)
#
# state = driver.find_element(By.NAME, "q9_address9[state]")
# state.is_displayed()
# print(f"state.is_displayed() --> {state.is_displayed()}")
# state.send_keys("Tamil nadu")
# print(f"The entered value is --> {state.get_attribute('value')}")
# time.sleep(2)
#
# postal_code = driver.find_element(By.NAME, "q9_address9[postal]")
# postal_code.is_displayed()
# print(f"postal_code.is_displayed() --> {postal_code.is_displayed()}")
# postal_code.send_keys("568421")
# print(f"The entered value is --> {postal_code.get_attribute('value')}")
# time.sleep(2)
#
# drop_down = driver.find_element(By.NAME, "q9_address9[country]")
# drop_down.is_displayed()
# print(f"drop_down.is_displayed() --> {drop_down.is_displayed()}")
#
# drop_down_selection = Select(drop_down)
# print(f"Total dropdown selection options are --> {len(drop_down_selection.options)}")
# drop_down_selection.select_by_visible_text("India")
#
# area_code = driver.find_element(By.NAME, "q5_phoneNumber5[area]")
# area_code.is_displayed()
# print(f"area_code.is_displayed() --> {area_code.is_displayed()}")
# area_code.send_keys("+91")
# print(f"The entered value is --> {area_code.get_attribute('value')}")
# time.sleep(2)
#
#
# phone_number = driver.find_element(By.NAME, "q5_phoneNumber5[phone]")
# phone_number.is_displayed()
# print(f"phone_number.is_displayed() --> {phone_number.is_displayed()}")
# phone_number.send_keys("8580369581")
# print(f"The entered value is --> {phone_number.get_attribute('value')}")
# time.sleep(2)
#
# # age_above_18 = driver.find_element(By.NAME, "form-radio validate[required] form-validation-error")
# # age_above_18.is_displayed()
# # print(f"age_above_18.is_displayed() --> {age_above_18.is_displayed()}")
# # age_above_18.click()
# # # print(f"The entered value is --> {postal_code.get_attribute('value')}")
# # time.sleep(1)
#
# where_did_you_here = driver.find_element(By.CSS_SELECTOR, "input[name='q16_whereDid']")
# where_did_you_here.is_displayed()
# print(f"where_did_you_here.is_displayed() --> {where_did_you_here.is_displayed()}")
# where_did_you_here.send_keys("I am here from particular website")
# print(f"The entered value is --> {postal_code.get_attribute('value')}")
# time.sleep(2)
#
# company = driver.find_element(By.NAME, "q13_companygrouporganization13")
# company.is_displayed()
# print(f"company.is_displayed() --> {company.is_displayed()}")
# company.send_keys("Jira")
# print(f"The entered value is --> {company.get_attribute('value')}")
# time.sleep(2)
#
# how_many_members = driver.find_element(By.NAME, "q14_howMembers14")
# how_many_members.is_displayed()
# print(f"how_many_members.is_displayed() --> {how_many_members.is_displayed()}")
# how_many_members.send_keys("5")
# print(f"The entered value is --> {how_many_members.get_attribute('value')}")
# time.sleep(2)
#
# driver.quit()




