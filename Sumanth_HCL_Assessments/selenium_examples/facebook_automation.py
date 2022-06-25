from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.facebook.com/")

account = driver.find_element(By.XPATH, "//*[text()='Create New Account']")
account.click()

print(driver.title)

time.sleep(5)

first_name = driver.find_element(By.NAME, "firstname")
first_name.send_keys("Sumanth")

# time.sleep(5)
#
# last_name = driver.find_element(By.NAME, "lastname")
# last_name.send_keys("Sumanth")
#
# time.sleep(5)
#
# email_address = driver.find_element(By.NAME, "reg_email__")
# email_address.send_keys("sumanth@gmail.com")
#
# time.sleep(5)
#
# re_enter_email_address = driver.find_element(By.NAME, "reg_email_confirmation__")
# re_enter_email_address.send_keys("sumanth@gmail.com")
#
# time.sleep(5)
#
# password = driver.find_element(By.ID, "password_step_input")
# password.send_keys("abcde")
#
# time.sleep(5)
#
# day = driver.find_element(By.NAME, "birthday_day")
# day.send_keys("9")
#
# time.sleep(5)
#
# month = driver.find_element(By.ID, "month")
# month.send_keys("May")
#
# time.sleep(5)
#
# year = driver.find_element(By.NAME, "birthday_year")
# year.send_keys("1999")
#
# time.sleep(5)
#
# # gender = driver.find_element(By.XPATH, "//*[@id='u_g_3_RN']")
# # gender.click()
#
# print("completed")


# driver.find_element(By.CLASS_NAME, "_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
# driver.find_element(By.ID, "u_0_2_7f']").click()

# driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("sumanth")

# time.sleep(5)

# driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys("sumanth")

# driver.close()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://facebook.com")
# driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()
# time.sleep(5)
# driver.find_element(By.NAME,"firstname").send_keys('kiran')
# time.sleep(5)
# driver.find_element(By.NAME,"lastname").send_keys('Achari')
# time.sleep(2)
# driver.find_element(By.NAME,"reg_email__").send_keys('kiranacharirk@gmail.com')
# time.sleep(10)
# driver.find_element(By.ID,"u_d_j_pF").send_keys('kirankn@gmail.com')
# driver.find_element(By.CSS_SELECTOR,'//*[@type="password"]').send_keys('422222221')
# time.sleep(3)
# #day
# dd = driver.find_element(By.ID,'day')
# day = Select(dd)
# day.select_by_value("25")
# #month
# mm = driver.find_element(By.ID,'month')
# mon = Select(mm)
# mon.select_by_visible_text('Oct')
# #year
# yy = driver.find_element(By.ID,'year')
# yer=Select(yy)
# yer.select_by_value('1996')
# #sex
# driver.find_element(By.ID,"u_d_5_GG").click()

# driver.quit()

