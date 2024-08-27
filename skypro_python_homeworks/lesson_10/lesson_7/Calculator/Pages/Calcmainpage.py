from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson_7.constants import Calculator_URL
import allure

class CalcMain:
    @allure.step("Открываем страницу с калькулятором")
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Calculator_URL)
    
    @allure.step("Вводим время ожидания")    
    def insert_time(self):
        delay_input = self.browser.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(45)
    
    @allure.step("Нажимаем кнопки калькулятора")            
    def clicking_buttons(self):
        self.browser.find_element(By.XPATH, "//span[text() = '7']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '+']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '8']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '=']").click()
    
    @allure.step("Ожидаем результат вычисления")      
    def wait_button_gettext(self):
        WebDriverWait(self.browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        return self.browser.find_element(By.CLASS_NAME, "screen").text 