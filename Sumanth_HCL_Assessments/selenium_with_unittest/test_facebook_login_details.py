import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FacebookTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        self.account = self.driver.find_element(By.XPATH, "//*[text()='Create New Account']")
        self.account.click()
        time.sleep(2)

    def test_title(self):
        title = "Facebook – log in or sign up"
        self.assertEqual(title, self.driver.title)

    def test_first_name(self):
        self.first_name = self.driver.find_element(By.NAME, "firstname")
        self.assertEqual(True, self.first_name.is_enabled())

    def test_last_name(self):
        self.last_name = self.driver.find_element(By.NAME, "lastname")
        self.assertEqual(True, self.last_name.is_enabled())

    def test_password(self):
        self.password = self.driver.find_element(By.ID, "password_step_input")
        self.assertEqual(True, self.password.is_enabled())

    def test_day(self):
        self.day = self.driver.find_element(By.NAME, "birthday_day")
        self.assertEqual(True, self.day.is_enabled())

    def test_month(self):
        self.month = self.driver.find_element(By.ID, "month")
        self.assertEqual(True, self.month.is_enabled())

    def test_year(self):
        self.year = self.driver.find_element(By.NAME, "birthday_year")
        self.assertEqual(True, self.year.is_enabled())

    def test_gender_male(self):
        self.gender_male = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input")
        self.assertEqual(True, self.gender_male.is_enabled())

    def test_signup(self):
        self.signup = self.driver.find_element(By.NAME, "websubmit")
        self.assertEqual(True, self.signup.is_enabled())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
