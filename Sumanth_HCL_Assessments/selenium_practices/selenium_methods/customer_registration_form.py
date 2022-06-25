# https://www.jotform.com/form-templates/new-customer-registration-form
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.jotform.com/build/221178469849472#preview")
print(f"Title of the page is --> {driver.title}")

# input_boxes = driver.find_elements(By.XPATH, "//input[@type='text']")
# # print(check_boxes)
# print(f"Available check boxes are --> {len(input_boxes)}")
# print(f"Current Page is --> {driver.title}")
# print(f"Current URL is --> {driver.current_url}")
#
first_name = driver.find_element(By.NAME, 'q3_fullName3[first]')
first_name.is_displayed()
print(f"first_name.is_displayed() --> {first_name.is_displayed()}")
first_name.send_keys("Ramesh")
print(f"The entered value in first name is --> {first_name.get_attribute('value')}")
time.sleep(2)
#
last_name = driver.find_element(By.NAME, 'q3_fullName3[last]')
last_name.is_displayed()
print(f"last_name.is_displayed() --> {last_name.is_displayed()}")
last_name.send_keys("Kumar")
print(f"The entered value in last name is --> {last_name.get_attribute('value')}")
time.sleep(2)

street_address_1 = driver.find_element(By.NAME, "q4_address4[addr_line1]")
street_address_1.is_displayed()
print(f"street_address_1.is_displayed() --> {street_address_1.is_displayed()}")
street_address_1.send_keys("Sri ram Nagar")
print(f"The entered value in street address 1 is --> {street_address_1.get_attribute('value')}")
time.sleep(2)

street_address_2 = driver.find_element(By.XPATH, "/html/body/form/div[1]/ul/li[3]/div/div[1]/div[2]/span/span/input")
street_address_2.is_displayed()
print(f"street_address_2.is_displayed() --> {street_address_2.is_displayed()}")
street_address_2.send_keys("Opposite to vijaya mahal")
print(f"The entered value in street address 2 is --> {street_address_2.get_attribute('value')}")
time.sleep(2)
#
city = driver.find_element(By.NAME, "q4_address4[city]")
city.is_displayed()
print(f"city.is_displayed() --> {city.is_displayed()}")
city.send_keys("Kurnool")
print(f"The entered value in city is --> {city.get_attribute('value')}")
time.sleep(2)
#
state = driver.find_element(By.NAME, "q4_address4[state]")
state.is_displayed()
print(f"state.is_displayed() --> {state.is_displayed()}")
state.send_keys("Tamil nadu")
print(f"The entered value in state is --> {state.get_attribute('value')}")
time.sleep(2)

postal_code = driver.find_element(By.NAME, "q4_address4[postal]")
postal_code.is_displayed()
print(f"postal_code.is_displayed() --> {postal_code.is_displayed()}")
postal_code.send_keys("569475")
print(f"The entered value in postal code is --> {postal_code.get_attribute('value')}")
time.sleep(2)

phone_number = driver.find_element(By.NAME, "q5_phoneNumber5[full]")
phone_number.is_displayed()
print(f"phone_number.is_displayed() --> {phone_number.is_displayed()}")
phone_number.send_keys("8580369581")
print(f"The entered value in phone number is --> {phone_number.get_attribute('value')}")
time.sleep(2)

gmail = driver.find_element(By.NAME, "q6_email6")
gmail.is_displayed()
print(f"gmail.is_displayed() --> {gmail.is_displayed()}")
gmail.send_keys("rameshkumar000@gmail.com")
print(f"The entered value in gmail is --> {gmail.get_attribute('value')}")
time.sleep(2)

how_did_you_hear_about_us = driver.find_element(By.NAME, "q8_howDid8")
print(f"application_type_drop_down.is_displayed() --> {how_did_you_hear_about_us.is_displayed()}")
how_did_you_hear_about_us_drop_down_selection = Select(how_did_you_hear_about_us)
print(f"Total Number of Application dropdown options are --> {len(how_did_you_hear_about_us_drop_down_selection.options)}")
print(f"--------------------------- Total Available Application dropdown options are ------------------------------ ")
for application_options in how_did_you_hear_about_us_drop_down_selection.options:
    print(application_options.text)
print("--------------------------------------------------------------------------------")
how_did_you_hear_about_us_drop_down_selection.select_by_index(2)

time.sleep(2)

feedback = driver.find_element(By.NAME, "q11_feedbackAbout11")
print(f"age_above_18.is_displayed() --> {feedback.is_displayed()}")
feedback.send_keys("Good")
print(f"The entered value in feedback is --> {feedback.get_attribute('value')}")
time.sleep(1)
#
#
suggestions = driver.find_element(By.NAME, "q12_suggestionsIf")
print(f"company.is_displayed() --> {suggestions.is_displayed()}")
suggestions.send_keys("Nothing")
print(f"The entered value in suggestions  is --> {suggestions.get_attribute('value')}")
time.sleep(2)
#

recommend = driver.find_element(By.XPATH, "/html/body/form/div[1]/ul/li[11]/div/div/span[2]/label")
print(f"recommend.is_displayed() --> {recommend.is_displayed()}")
# recommend.click()
# time.sleep(2)

driver.quit()



