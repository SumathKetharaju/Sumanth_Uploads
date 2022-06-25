from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class Search(unittest.TestCase):

    def setup(self):
        self.local_driver = webdriver.Chrome()
        self.local_driver.implicitly_wait(3)
        self.local_driver.maximize_window()

        self.local_driver.get("https://www.google.com/")

    def test_search_by_test(self):

        self.search_filed = self.local_driver.find_element(By.NAME, "q")
        self.search_filed.send_keys("Selenium Webdriver Interview Questions")
        self.search_filed.submit()
        lists = self.local_driver.find_element(By.CLASS_NAME, "r")
        length = len(lists)
        self.assertEqual(17, len(lists))

    def teardown(self):
        self.local_driver.quit()


if __name__ == "__main__":
    unittest.main()

