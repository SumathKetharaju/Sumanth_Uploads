from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# It opens the browser
driver = webdriver.Chrome()

driver.maximize_window()

# Target URL
driver.get("https://www.programiz.com/python-programming")

print(f"Title of the page is --> {driver.title}")

# Printing the whole body text
programiz_page = driver.find_element(By.XPATH, "/html/body")
print(f"programiz_page.is_displayed() --> {programiz_page.is_displayed()}")

python_content = programiz_page.text

# print(python_content)

with open("programiz_content.txt", "w") as f:
    f.write(python_content)

