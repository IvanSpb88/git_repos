from selenium.webdriver.common.by import By
from lesson_7.constants import Test_form_URL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage:
    def __init__(self, browser, url=Test_form_URL):
        self.browser = browser
        self.url = url
    
    def  open(self):
        self.browser.get(self.url)
    
    def fill_fields(self, v_dict: dict):
        for key, value in v_dict.items():
            selector = f'[name={key}]'
            self.browser.find_element(By.CSS_SELECTOR, selector).send_keys(value)

    def click_submit(self):
         WebDriverWait(self.browser, 40, 0.1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))).click()
        
    def find_element_property(self, locator):
        background_color = self.browser.find_element(By.ID, locator).value_of_css_property("background-color")
        return background_color