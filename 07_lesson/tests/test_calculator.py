from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


def test_calculator():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    page = CalculatorPage(driver)

    page.open()
    page.set_delay("45")

    page.press_button("7")
    page.press_button("+")
    page.press_button("8")
    page.press_button("=")

    page.wait_result("15")
    assert page.get_result() == "15"

    driver.quit()
