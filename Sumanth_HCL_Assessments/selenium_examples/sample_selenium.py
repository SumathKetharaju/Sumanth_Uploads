from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

print("Sample test case started")

# driver_service = Service()  # if the driver.exe is in our current directory it is fine
# driver = webdriver.Chrome(driver_service)  # exactly not valid

# if the driver.exe is in our current directory, driver_service is not mandatory else driver_service is mandatory
# driver_service = Service(r"C:\Selenium_data\chromedriver.exe")

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://www.google.com/")

print(f"Title of the page is --> {driver.title}")

print(f"Current URl --> {driver.current_url}")

print(f"html code for the current page --> {driver.page_source}")

driver.close()





"""
driver = webdriver.Chrome(executable_path=r"C:\Selenium_data\chromedriver.exe")
driver.get("http://www.google.com")
driver.maximize_window()
print(driver.title)
driver.close()

output -->
warning --> DeprecationWarning: executable_path has been deprecated, please pass in a Service object
Google
Success
"""

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome(executable_path=r"C:\Users\SUMANTH\Desktop\Selenium_Drives\chromedriver_win32.exe")
#
# driver.get("http://newtours.demoaut.com/")
#
# print(driver.title)
#
# driver.close()
