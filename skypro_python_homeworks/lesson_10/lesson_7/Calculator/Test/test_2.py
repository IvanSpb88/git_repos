from lesson_7.Calculator.Pages.Calcmainpage import CalcMain
import allure

@allure.epic("Calculator")
@allure.severity(severity_level="normal")
@allure.title("Работа калькулятора")
@allure.description("Поиск полей ввод данных и вывод результата вычисления")
@allure.feature('Тест 1')
def test_calculator_assert(chrome_browser):
    with allure.step("Открываем страницу с калькулятором"):
        calcmain = CalcMain(chrome_browser)
    with allure.step("Вводим время ожидания"):
        calcmain.insert_time()
    with allure.step("Нажимаем кнопки калькулятора"):
        calcmain.clicking_buttons()
    with allure.step("Ожидаем результат вычисления"):
        assert "15" in calcmain.wait_button_gettext()