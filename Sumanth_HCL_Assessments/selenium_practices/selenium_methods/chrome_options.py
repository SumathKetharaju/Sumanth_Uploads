# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options #object of Options class
# c = Options()
# # passing headless parameter
# c.add_argument("--headless")
# # adding headless parameter to webdriver object
# driver = webdriver.Chrome(options=c)
# # implicit wait time
# driver.implicitly_wait(5)
# # url launch
# driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
# print('Page title: ' + driver.title)
# # driver quit driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
#object of ChromeOptions
op = webdriver.ChromeOptions()
#add option
op.add_argument('--enable-extensions')
#pass option to webdriver object
driver = webdriver.Chrome(options=op)
print("completed")

