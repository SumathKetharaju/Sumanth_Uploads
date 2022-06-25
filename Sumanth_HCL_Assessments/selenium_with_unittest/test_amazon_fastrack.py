import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class AmazonFastrackWatch(unittest.TestCase):

    def setUp(self):
        self.local_driver = webdriver.Chrome()
        self.local_driver.implicitly_wait(2)
        self.local_driver.maximize_window()
        self.local_driver.get("https://www.amazon.in/")
        time.sleep(2)

    def test_amazon_title(self):
        amazon_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
        self.assertEqual(amazon_title, self.local_driver.title)

    def test_search_bar(self):
        self.search_bar = self.local_driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
        self.assertEqual(True, self.search_bar.is_displayed())

    def test_search_submit_button(self):
        self.search_submit_button = self.local_driver.find_element(By.ID, 'nav-search-submit-button')
        self.assertEqual(True, self.search_submit_button.is_displayed())

    def test_fastrack_watch(self):
        self.search_bar_2 = self.local_driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
        self.search_bar_2.send_keys("top 10 watch for men")
        time.sleep(2)
        self.search_submit_button_2 = self.local_driver.find_element(By.ID, 'nav-search-submit-button')
        self.search_submit_button_2.click()
        time.sleep(2)
        self.fastrack_watch = self.local_driver.find_element(By.XPATH, '//*[@id="p_89/Fastrack"]/span/a/div/label/i')
        self.assertEqual(True, self.fastrack_watch.is_displayed())

    def test_casio_analog_watch(self):
        self.search_bar_2 = self.local_driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
        self.search_bar_2.send_keys("top 10 watch for men")
        time.sleep(2)
        self.search_submit_button_2 = self.local_driver.find_element(By.ID, 'nav-search-submit-button')
        self.search_submit_button_2.click()
        time.sleep(2)
        self.fastrack_watch = self.local_driver.find_element(By.XPATH, '//*[@id="p_89/Fastrack"]/span/a/div/label/i')
        self.fastrack_watch.click()
        self.casio_analog_watch = self.local_driver.find_element(By.XPATH, """//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/
        div/div[2]/div[1]/h2/a/span""")
        self.assertEqual(True, self.casio_analog_watch.is_displayed())

    def tearDown(self):
        self.local_driver.quit()


if __name__ == "__main__":
    unittest.main()

