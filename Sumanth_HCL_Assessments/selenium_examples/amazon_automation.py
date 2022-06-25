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
search.send_keys("Top 10 mobiles in 2022")
time.sleep(2)

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")

search_bar = local_driver.find_element(By.ID, 'nav-search-submit-button')
print(f"search_bar.is_displayed() --> {search_bar.is_displayed()}")
search_bar.click()

time.sleep(2)
print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")

vivo = local_driver.find_element(By.XPATH, '//*[@id="p_89/Vivo"]/span/a/div/label/i')
print(f"vivo.is_displayed() --> {vivo.is_displayed()}")
vivo.click()

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")
time.sleep(2)

vivo_v21 = local_driver.find_element(By.XPATH, """//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/
div/div/div/div[2]/div/div/div[1]/h2/a/span""")

print(f"vivo_v21.is_displayed() --> {vivo_v21.is_displayed()}")
vivo_v21.click()

print(f"Current Page is --> {local_driver.title}")
print(f"Current URL is --> {local_driver.current_url}")
print("Sample test case Completed")

local_driver.close()

# mobile = local_driver.find_element(By.CLASS_NAME, "nav-a  ")
# mobile.is_displayed()
# print(f"mobile.is_displayed() --> {mobile.is_displayed()}")
# mobile.click()


