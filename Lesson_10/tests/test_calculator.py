import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.calculator_page import CalculatorPage


@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка сложения")
@allure.description("Проверка корректного вычисления 7 + 8")
def test_calculator():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    page = CalculatorPage(driver)

    with allure.step("Открыть страницу"):
        page.open()

    with allure.step("Установить задержку"):
        page.set_delay("45")

    with allure.step("Выполнить вычисление"):
        page.press_button("7")
        page.press_button("+")
        page.press_button("8")
        page.press_button("=")

    with allure.step("Ожидание результата"):
        page.wait_result("15")

    with allure.step("Проверка результата"):
        assert page.get_result() == "15"

    driver.quit()
