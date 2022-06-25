import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Sample test case started")

local_driver = webdriver.Chrome()

local_driver.maximize_window()

local_driver.get("https://www.amazon.in/")
time.sleep(2)
print(f"Current Page after opening amazon link is --> {local_driver.title}")
print(f"Current URL after opening amazon link is --> {local_driver.current_url}")


search_bar = local_driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
search_bar.is_displayed()
search_bar.send_keys("Top 10 mobiles in 2022")
time.sleep(2)
print(f"Entered value in search bar is --> {search_bar.get_attribute('value')}")


search_button = local_driver.find_element(By.ID, 'nav-search-submit-button')
print(f"search_button.is_displayed() --> {search_button.is_displayed()}")
search_button.click()
time.sleep(2)
print(f"Current Page after clicking on search button is --> {local_driver.title}")
print(f"Current URL after clicking on search button is --> {local_driver.current_url}")

vivo_brand = local_driver.find_element(By.XPATH, '//*[@id="p_89/Vivo"]/span/a/div/label/i')
print(f"vivo_brand.is_displayed() --> {vivo_brand.is_displayed()}")
vivo_brand.click()
time.sleep(2)
print(f"Current Page after clicking on Vivo brand is --> {local_driver.title}")
print(f"Current URL after clicking on Vivo brand is --> {local_driver.current_url}")


vivo_v15_pro_mobile = local_driver.find_element(By.XPATH, """//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/
div/div/div/div[2]/div/div/div[1]/h2/a/span""")
print(f"vivo_v15_pro_mobile.is_displayed() --> {vivo_v15_pro_mobile.is_displayed()}")
print(f"Name of the Mobile is --> {vivo_v15_pro_mobile.text}")
vivo_v15_pro_mobile.click()
time.sleep(2)
print(f"Current Page after clicking on vivo_v15_pro mobile is --> {local_driver.title}")
print(f"Current URL after clicking on vivo_v15_pro mobile is --> {local_driver.current_url}")

cost_of_vivo_v15_pro = local_driver.find_element(By.XPATH, """//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/
div[11]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span[1]/span[2]/span[2]""")
print(f"Cost of Vivo v15_pro.is_displayed() --> {cost_of_vivo_v15_pro.is_displayed()}")
print(f"Cost of Vivo V15 pro mobile is --> {cost_of_vivo_v15_pro.text}")

parent_window = local_driver.current_window_handle
print(f"Current window handle is --> {parent_window}")

windows = local_driver.window_handles
print(f"Current all window handles is --> {windows}")

for handle in local_driver.window_handles:
    # print("success")
    print(f"each window handle in windows is --> {handle}")
    if handle != parent_window:
        child_window = handle
        local_driver.switch_to.window(child_window)
        time.sleep(2)
        print(f"Current Page after switching child window is --> {local_driver.title}")
        print(f"Current URL after switching child window  is --> {local_driver.current_url}")
        print("-------------------------------------success in switch---------------------------------------------")
        local_driver.switch_to.window(parent_window)
        time.sleep(2)
        print(f"Current Page after switching Parent window  is --> {local_driver.title}")
        print(f"Current URL after switching Parent window  is --> {local_driver.current_url}")
        local_driver.back()
        time.sleep(2)
        print(f"Current Page after using backward navigation is --> {local_driver.title}")
        print(f"Current URL after using backward navigation is --> {local_driver.current_url}")

        oppo_brand = local_driver.find_element(By.XPATH, '//*[@id="p_89/Oppo"]/span/a/div/label/i')
        print(f"oppo_brand.is_displayed() --> {oppo_brand.is_displayed()}")
        oppo_brand.click()
        time.sleep(2)
        print(f"Current Page after clicking on Oppo brand is --> {local_driver.title}")
        print(f"Current URL after clicking on Oppo brand is --> {local_driver.current_url}")

        oppo_f19_pro_mobile = local_driver.find_element(By.XPATH, """//*[@id="search"]/div[1]/div[1]/div/span[3]/
        div[2]/div[22]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span""")
        print(f"oppo_f19_pro_mobile.is_displayed() --> {oppo_f19_pro_mobile.is_displayed()}")
        print(f"Name of the Mobile is --> {oppo_f19_pro_mobile.text}")
        oppo_f19_pro_mobile.click()
        time.sleep(2)
        print(f"Current Page after clicking on oppo_f19_pro mobile is --> {local_driver.title}")
        print(f"Current URL after clicking on oppo_f19_pro mobile is --> {local_driver.current_url}")

        cost_of_oppo_f19_pro = local_driver.find_element(By.XPATH, """//*[@id="search"]/div[1]/div[1]/div/span[3]/
        div[2]/div[22]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span[1]/span[2]/span[2]""")
        print(f"cost_of_oppo_f19_pro.is_displayed() --> {cost_of_oppo_f19_pro.is_displayed()}")
        print(f"cost_of_oppo_f19_pro.text --> {cost_of_oppo_f19_pro.text}")
        time.sleep(5)
        local_driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.maximize_window()
#
# driver.get("https://www.amazon.in/")
# print(f"Title of the page is --> {driver.title}")
#
# search_bar = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
# search_bar.is_displayed()
# print(f"search.is_displayed() --> {search_bar.is_displayed()}")
# search_bar.send_keys("Top 10 mobiles in 2022")
# # time.sleep(2)
#
# print(f"Current Page is --> {driver.title}")
# print(f"Current URL is --> {driver.current_url}")
#
# search_button = driver.find_element(By.ID, 'nav-search-submit-button')
# print(f"search_button.is_displayed() --> {search_button.is_displayed()}")
# search_button.click()
# print(f"Current Page is --> {driver.title}")
# print(f"Current URL is --> {driver.current_url}")
#
# samsung_xpath = driver.find_element(By.XPATH, "//*[@id='p_89/Samsung']/span/a/div/label/i")
# print(f"samsung_xpath.is_displayed() --> {samsung_xpath.is_displayed()}")
# samsung_xpath.click()
# print(f"Current Page is --> {driver.title}")
# print(f"Current URL is --> {driver.current_url}")
#
# # samsung_mobile = driver.find_element(By.XPATH, """//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/
# # div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span""")
# # print(f"samsung_mobile.is_displayed() --> {samsung_xpath.is_displayed()}")
# # samsung_mobile.click()
# # print(f"Current Page is --> {driver.title}")
# # print(f"Current URL is --> {driver.current_url}")
#
# crt_window = driver.current_window_handle
# print(f"current window handle is {crt_window}")



































# driver = webdriver.Chrome()  # implicit wait time
# driver.maximize_window()
# driver.implicitly_wait(5)  # url launch
# driver.get("https://the-internet.herokuapp.com/windows")  # identify element
# s = driver.find_element(By.LINK_TEXT, "Click Here")
# s.click()
# print('Page title of new tab: ' + driver.title)
# # current main window handle
# m = driver.current_window_handle
# print(m)
# # iterate over all window handles
# for h in driver.window_handles:
#     print(h)
#
#     if h != m:
#         print('Page title of new tab: ' + driver.title)
#         n = h
#         print(n)
#         driver.switch_to.window(n)
#         print('Page title of new tab: ' + driver.title)  # switch to main window driver.switch_to.window(m)
# print('Page title of main window: ' + driver.title)  # quit browser
# # driver.quit()
