import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class SandDiskPendrive(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.in/")
        time.sleep(2)

    def test_amazon_title(self):
        amazon_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
        self.assertEqual(amazon_title, self.driver.title)

    def test_search_bar(self):
        search_bar = self.driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
        self.assertEqual(True, search_bar.is_displayed())

    def test_search_submit_button(self):
        search_submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[id='nav-search-submit-button']")
        self.assertEqual(True, search_submit_button.is_displayed())

    def test_sand_disk_pendrive(self):
        search_bar = self.driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
        search_bar.send_keys("Top 10 Sand disk Pendrives under 1000")
        time.sleep(2)
        search_submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[id='nav-search-submit-button']")
        search_submit_button.click()
        time.sleep(2)
        sand_disk_all_data = self.driver.find_element(By.CLASS_NAME, "sg-col-inner")
        self.assertEqual(True, sand_disk_all_data.is_displayed())

    def test_sand_disk_32_gb(self):
        search_bar = self.driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
        search_bar.send_keys("Top 10 Sand disk Pendrives under 1000")
        time.sleep(2)
        search_submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[id='nav-search-submit-button']")
        search_submit_button.click()
        time.sleep(2)
        sand_disk_all_data = self.driver.find_element(By.CLASS_NAME, "sg-col-inner")
        sand_disk_all_data.click()
        sand_disk_32_gb = self.driver.find_element(By.LINK_TEXT, "SanDisk Cruzer Blade 32GB USB Flash Drive")
        self.assertEqual(True, sand_disk_32_gb.is_displayed())

    def test_sand_disk_32_gb_details(self):
        search_bar = self.driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
        search_bar.send_keys("Top 10 Sand disk Pendrives under 1000")
        time.sleep(2)
        search_submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[id='nav-search-submit-button']")
        search_submit_button.click()
        time.sleep(2)
        sand_disk_all_data = self.driver.find_element(By.CLASS_NAME, "sg-col-inner")
        sand_disk_all_data.click()
        sand_disk_32_gb = self.driver.find_element(By.LINK_TEXT, "SanDisk Cruzer Blade 32GB USB Flash Drive")
        sand_disk_32_gb.click()
        sand_disk_32_gb_details = self.driver.find_element(By.CLASS_NAME, "a-size-base")
        self.assertEqual(True, sand_disk_32_gb_details.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

