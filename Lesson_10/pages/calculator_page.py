from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Page Object для страницы калькулятора.
    """

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.ID, "delay")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None
        """
        self.driver.get(self.URL)

    def set_delay(self, value: str) -> None:
        """
        Устанавливает задержку вычислений.

        :param value: значение задержки
        :type value: str
        :return: None
        """
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(value)

    def press_button(self, value: str) -> None:
        """
        Нажимает кнопку калькулятора.

        :param value: текст кнопки
        :type value: str
        :return: None
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']"
        )
        button.click()

    def get_result(self) -> str:
        """
        Получает результат вычисления.

        :return: результат
        :rtype: str
        """
        return self.driver.find_element(*self.RESULT).text

    def wait_result(self, value: str, timeout: int = 50) -> bool:
        """
        Ожидает появления результата.

        :param value: ожидаемый результат
        :type value: str
        :param timeout: время ожидания
        :type timeout: int
        :return: True если текст появился
        :rtype: bool
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.text_to_be_present_in_element(self.RESULT, value)
        )
