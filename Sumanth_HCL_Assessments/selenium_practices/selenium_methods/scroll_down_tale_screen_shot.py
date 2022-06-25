from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)
print(f"Tile of the page is --> {driver.title}")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(1)
print(f"Tile of the page is --> {driver.title}")


# Scroll down page till element found
india_flag = driver.find_element(By.CSS_SELECTOR, 'img[alt="Flag of India"]')
driver.execute_script("arguments[0].scrollIntoView();", india_flag)

driver.save_screenshot(r"C:\Users\SUMANTH\Desktop\Automation_Purposes\Automations\indian_flag.png")

# scroll down page till end
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

