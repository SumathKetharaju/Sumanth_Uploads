import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.in/")

    def test_amazon_title(self):
        self.assertEqual(self.driver.title, "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")

    def test_payment_options(self):
        self.amazon_pay = self.driver.find_element(By.LINK_TEXT, "Amazon Pay")
        time.sleep(2)
        self.amazon_pay.click()
        time.sleep(2)

        pay_options = self.driver.find_elements(By.CLASS_NAME, "image-footer-text-desktop")
        number_of_pay_options = len(pay_options)
        self.assertEqual(42, number_of_pay_options)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

