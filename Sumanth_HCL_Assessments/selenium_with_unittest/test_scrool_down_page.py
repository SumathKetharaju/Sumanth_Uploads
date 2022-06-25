import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CustomerRegistrationForm(unittest.TestCase):

    def setUp(self):
        path = r"https://www.countries-ofthe-world.com/flags-of-the-world.html"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get(path)
        time.sleep(2)

    def test_title_countries(self):
        title = "Country flags of the world with images and names"
        self.assertEqual(title, self.driver.title)

    def test_indian_flag(self):
        india_flag = self.driver.find_element(By.CSS_SELECTOR, 'img[alt="Flag of India"]')
        self.assertEqual(True, india_flag.is_displayed())

    def test_scroll_down_tii_indian_flag(self):
        india_flag = self.driver.find_element(By.CSS_SELECTOR, 'img[alt="Flag of India"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", india_flag)

    def test_scroll_down_tii_end_of_page(self):
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

