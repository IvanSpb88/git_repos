from selenium import webdriver 
from time import sleep

driver = webdriver.Chrome ()

try:
    
    driver.get("http://uitestingplayground.com/textinput")
    button_name = driver.find_element(
    "id", "newButtonName").send_keys("SkyPro")
    sleep(2)
    confirm_button_name = driver.find_element("id", "updatingButton").click()
    sleep(2)
    new_button_name = driver.find_element("id", "updatingButton").text
    sleep(2)
    print(new_button_name)   
finally:
    driver.quit()