import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CustomerRegistrationForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get("https://www.jotform.com/build/221178469849472#preview")
        time.sleep(2)

    def test_title_customer(self):
        title = "New Customer Registration Form"
        self.assertEqual(title, self.driver.title)

    def test_first_name(self):
        first_name = self.driver.find_element(By.NAME, 'q3_fullName3[first]')
        self.assertEqual(True, first_name.is_displayed())

    def test_last_name(self):
        last_name = self.driver.find_element(By.NAME, 'q3_fullName3[last]')
        self.assertEqual(True, last_name.is_displayed())

    def test_street_address_1(self):
        street_address_1 = self.driver.find_element(By.NAME, "q4_address4[addr_line1]")
        self.assertEqual(True, street_address_1.is_displayed())

    def test_city(self):
        city = self.driver.find_element(By.NAME, "q4_address4[city]")
        self.assertEqual(True, city.is_displayed())

    def test_state(self):
        state = self.driver.find_element(By.NAME, "q4_address4[state]")
        self.assertEqual(True, state.is_displayed())

    def test_postal_code(self):
        postal_code = self.driver.find_element(By.NAME, "q4_address4[postal]")
        self.assertEqual(True, postal_code.is_displayed())

    def test_phone_number(self):
        phone_number = self.driver.find_element(By.NAME, "q5_phoneNumber5[full]")
        self.assertEqual(True, phone_number.is_displayed())

    def test_gmail(self):
        gmail = self.driver.find_element(By.NAME, "q6_email6")
        self.assertEqual(True, gmail.is_displayed())

    def test_how_did_you_hear_about_us(self):
        how_did_you_hear_about_us = self.driver.find_element(By.NAME, "q8_howDid8")
        self.assertEqual(True, how_did_you_hear_about_us.is_displayed())

    def test_options_in_how_did_you_hear_about_us(self):
        how_did_you_hear_about_us = self.driver.find_element(By.NAME, "q8_howDid8")
        how_did_you_hear_about_us_drop_down_selection = Select(how_did_you_hear_about_us)
        length = len(how_did_you_hear_about_us_drop_down_selection.options)
        self.assertEqual(5, length)

    def test_feedback(self):
        feedback = self.driver.find_element(By.NAME, "q11_feedbackAbout11")
        self.assertEqual(True, feedback.is_displayed())

    def test_suggestions(self):
        suggestions = self.driver.find_element(By.NAME, "q12_suggestionsIf")
        self.assertEqual(True, suggestions.is_displayed())

    def test_recommend(self):
        recommend = self.driver.find_element(By.XPATH, "/html/body/form/div[1]/ul/li[11]/div/div/span[2]/label")
        self.assertEqual(True, recommend.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

