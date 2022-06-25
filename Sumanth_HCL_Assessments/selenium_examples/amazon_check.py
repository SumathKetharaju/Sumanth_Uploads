import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Sample test case started")

local_driver = webdriver.Chrome()

local_driver.maximize_window()

local_driver.get("https://www.amazon.in/")

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")
time.sleep(2)

search = local_driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
search.is_displayed()
print(f"search.is_displayed() --> {search.is_displayed()}")
search.send_keys("top 10 watch for men")
time.sleep(2)

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")

search_bar = local_driver.find_element(By.ID, 'nav-search-submit-button')
print(f"search_bar.is_displayed() --> {search_bar.is_displayed()}")
search_bar.click()

time.sleep(2)
print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")

Fastrack = local_driver.find_element(By.XPATH, '//*[@id="p_89/Fastrack"]/span/a/div/label/i')
print(f"Fastrack.is_displayed() --> {Fastrack.is_displayed()}")
Fastrack.click()

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")
time.sleep(2)

casio_analog_watch = local_driver.find_element(By.XPATH, """//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/
div/div[2]/div[1]/h2/a/span""")

print(f"one_plus.is_displayed() --> {casio_analog_watch.is_displayed()}")
casio_analog_watch.click()

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")
print("Sample test case Completed")

# local_driver.close()
time.sleep(2)
local_driver.quit()


