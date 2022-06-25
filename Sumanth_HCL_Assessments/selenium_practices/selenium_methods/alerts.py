from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
print(f"Title of the page is --> {driver.title}")

alert = driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button')
print(f"Title of the page is --> {driver.title}")
print(f"alert.is_displayed() --> {alert.is_displayed()}")
alert.click()

alert = Alert(driver)
print(alert.text)
alert.dismiss()

# alert.accept()

driver.quit()



# driver.switch_to_alert().dismiss()


