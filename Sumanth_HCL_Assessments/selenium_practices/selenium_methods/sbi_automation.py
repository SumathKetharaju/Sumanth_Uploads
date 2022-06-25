from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.onlinesbi.com/personal/")
time.sleep(2)
print(f"title of the page is --> {driver.title}")

# UserWarning: name used for saved screenshot does not match file type. It should end with a `.png` extension
# warnings.warn("name used for saved screenshot does not match file "
# driver.save_screenshot(r"C:\Users\SUMANTH\Desktop\Automation_Purposes\Automations\SBI_Front_Page.jpg")

# driver.save_screenshot(r"C:\Users\SUMANTH\Desktop\Automation_Purposes\Automations\SBI_Front_Page.png")

products_and_services = driver.find_element(By.LINK_TEXT, 'Products and Services')
print(f"products_and_services.is_displayed() --> {products_and_services.is_displayed()}")
products_and_services.click()
time.sleep(2)

# driver.get_screenshot_as_file(r"C:\Users\SUMANTH\Desktop\Automation_Purposes\Automations\SBI_products_and_services.png")

credit_card = driver.find_element(By.XPATH, '//*[@id="tab_2"]/div[1]/ul[1]/li/ul/li[4]/a')
print(f"credit_card.is_displayed() --> {credit_card.is_displayed()}")
credit_card.click()
time.sleep(2)

driver.get_screenshot_as_file(r"C:\Users\SUMANTH\Desktop\Automation_Purposes\Automations\SBI_credit_card_2.png")
time.sleep(2)

driver.quit()

# merchant_list_for_online_payments = driver.find_element(By.XPATH, '//*[@id="merchant"]')
# print(f"merchant_list_for_online_payments.is_displayed() --> {merchant_list_for_online_payments.is_displayed()}")
# merchant_list_for_online_payments.click()
# time.sleep(2)

# driver.save_screenshot(r"C:\Users\SUMANTH\Desktop\Automation_Purposes\Automations\merchant_list_for_online_payments.png")

# services = driver.find_element(By.XPATH, '//*[@id="navband"]/ul/li[5]/a')
# print(f"government.is_displayed() --> {services.is_displayed()}")
# services.click()
# time.sleep(2)
