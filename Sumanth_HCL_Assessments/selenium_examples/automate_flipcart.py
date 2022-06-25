import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Sample test case started")

local_driver = webdriver.Chrome()

local_driver.maximize_window()

local_driver.get("https://www.flipkart.com/")

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")
time.sleep(2)

close_wondow = local_driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button')
close_wondow.is_displayed()
print(f"close_wondow.is_displayed() --> {close_wondow.is_displayed()}")
close_wondow.click()
time.sleep(2)

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")


Top_offers = local_driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div/div[1]/a/div[1]/div/img')
Top_offers.is_displayed()
print(f"Top_offers.is_displayed() --> {Top_offers.is_displayed()}")
Top_offers.click()
time.sleep(2)

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")

Watch = local_driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div[5]/div/a/div[2]')
Watch.is_displayed()
print(f"Watch.is_displayed() --> {Watch.is_displayed()}")
Watch.click()
time.sleep(2)

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")

print("Sample test case Completed")

local_driver.close()



