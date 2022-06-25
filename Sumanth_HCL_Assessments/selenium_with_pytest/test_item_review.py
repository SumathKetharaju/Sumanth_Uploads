import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def setup():
    print("Setup method will execute before every testcase")
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    time.sleep(2)


def test_title_of_the_page():
    title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    assert driver.title == title


# def test_add_float():
#     result = math_func.add(3.2, 2.4)
#     assert result == 5.6
#
#
# def test_add_string():
#     result = math_func.add("winter ", "season")
#     assert result == "winter season"