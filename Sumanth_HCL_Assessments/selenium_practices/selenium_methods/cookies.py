from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
# url launch
# driver.get("https://www.tutorialspoint.com/index.htm")
driver.get("https://www.browserstack.com/guide/how-to-find-broken-links-in-selenium")
time.sleep(2)
# add a cookie
# c = {'name': 'c1', 'value': 'val1'}
time.sleep(2)
# # get a cookie
l = driver.get_cookies()
time.sleep(2)
# print('Cookie is: ')
# print(l)
driver.delete_all_cookies()
print(l)
# # get all cookies
# m = driver.get_cookies()
# time.sleep(2)
# print('Cookies are: ')
# print(m)
# delete a cookie
# driver.delete_cookie('c1') #check cookie after deletion
