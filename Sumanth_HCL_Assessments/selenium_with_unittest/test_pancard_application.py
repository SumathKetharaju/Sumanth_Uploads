import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PanCardApplication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get("https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html")
        time.sleep(2)

    def test_pancard_application_url(self):
        pancard_application_url = "https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html"
        self.assertEqual(pancard_application_url, self.driver.current_url)

    def test_application_type_drop_down(self):
        application_type_drop_down = self.driver.find_element(By.XPATH, '//*[@id="type"]')
        self.assertEqual(True, application_type_drop_down.is_displayed())

    def test_number_of_application_type_drop_downs(self):
        application_type_drop_down = self.driver.find_element(By.XPATH, '//*[@id="type"]')
        application_type_drop_down_selection = Select(application_type_drop_down)
        number_of_application_type_drop_downs = len(application_type_drop_down_selection.options)
        self.assertEqual(4, number_of_application_type_drop_downs)

    def test_category_type_drop_downs(self):
        category_drop_down = self.driver.find_element(By.XPATH, '//*[@id="cat_applicant1"]')
        self.assertEqual(True, category_drop_down.is_displayed())

    def test_number_of_category_type_drop_downs(self):
        category_drop_down = self.driver.find_element(By.XPATH, '//*[@id="cat_applicant1"]')
        category_drop_down_selection = Select(category_drop_down)
        number_of_category_drop_down_selection = len(category_drop_down_selection.options)
        self.assertEqual(12, number_of_category_drop_down_selection)

    def test_titles_drop_downs(self):
        titles_drop_down = self.driver.find_element(By.XPATH, '//*[@id="rvNameInitials"]')
        self.assertEqual(True, titles_drop_down.is_displayed())

    def test_number_of_titles_drop_downs(self):
        titles_drop_down = self.driver.find_element(By.XPATH, '//*[@id="rvNameInitials"]')
        titles_drop_down_selection = Select(titles_drop_down)
        number_of_titles_drop_downs_selection = len(titles_drop_down_selection.options)
        self.assertNotEqual(4, number_of_titles_drop_downs_selection)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

