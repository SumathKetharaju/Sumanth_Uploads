from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.geeksforgeeks.org/")

add_cooks = driver.add_cookie({"name": "foo", "value": "bar"})

print(add_cooks)

get_cooks = driver.get_cookie("foo")

print(get_cooks)

print(driver.get_cookies())

# delete browser cookie
driver.delete_cookie("foo")

