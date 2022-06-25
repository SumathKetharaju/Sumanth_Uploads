# from selenium import webdriver
# from selenium.webdriver.support.color import Color
# # color conversion to rgba format
# #
# print(Color.from_string('#00fe37').rgba)
# # color conversion to hex format
# print(Color.from_string('rgb(1, 200, 5)').hex)
# # color conversion to rgba format
# print(Color.from_string('green').rgba)


from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome() #implicit wait time
driver.implicitly_wait(5) #url launch
driver.get("https://the-internet.herokuapp.com/nested_frames") #switch to frame
driver.switch_to.frame('frame-bottom') #identify source element
s = driver.find_element(By.TAG_NAME, "body") #obtain text
t = s.text
print('Text is: ' + t) #quit browser driver.quit()

