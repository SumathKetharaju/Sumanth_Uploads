# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# create webdriver object
driver = webdriver.Chrome(ChromeDriverManager().install())

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_link_text("Courses")

# create action chain object
action = ActionChains(driver)

# context click the item
action.context_click(on_element=element)

# perform the operation
action.perform()

driver.close()
