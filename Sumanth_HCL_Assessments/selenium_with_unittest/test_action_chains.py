import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class PythonProgramiz(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get("https://www.programiz.com/python-programming")
        time.sleep(2)

    def test_programiz_title(self):
        programiz_title = "Learn Python Programming"
        self.assertEqual(programiz_title, self.driver.title)

    def test_functions(self):
        functions = self.driver.find_element(By.XPATH, "/html/body/main/div[7]/div/div/div/div/div[1]/div[1]/div/ul/li[3]/a")
        self.assertEqual(True, functions.is_displayed())

    def test_move_to_element(self):
        functions = self.driver.find_element(By.XPATH,"/html/body/main/div[7]/div/div/div/div/div[1]/div[1]/div/ul/li[3]/a")
        action = ActionChains(self.driver)
        action.move_to_element(functions)
        time.sleep(2)
        action.perform()
        self.assertEqual("Function", functions.text)

    def test_global_keyword(self):
        functions = self.driver.find_element(By.XPATH,"/html/body/main/div[7]/div/div/div/div/div[1]/div[1]/div/ul/li[3]/a")
        action = ActionChains(self.driver)
        time.sleep(2)
        action.move_to_element(functions)
        time.sleep(2)
        python_global_keyword = self.driver.find_element(By.XPATH, "/html/body/main/div[7]/div/div/div/div/div[2]/div[5]/div/div/ul/li[5]/a")
        action.perform()
        self.assertEqual(True, python_global_keyword.is_displayed())

    def test_action_on_global_keyword(self):
        functions = self.driver.find_element(By.XPATH,"/html/body/main/div[7]/div/div/div/div/div[1]/div[1]/div/ul/li[3]/a")
        action = ActionChains(self.driver)
        time.sleep(2)
        action.move_to_element(functions)
        time.sleep(2)
        python_global_keyword = self.driver.find_element(By.XPATH, "/html/body/main/div[7]/div/div/div/div/div[2]/div[5]/div/div/ul/li[5]/a")
        action.click(python_global_keyword)
        action.perform()
        self.assertEqual("Global, Local and Nonlocal", python_global_keyword.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

