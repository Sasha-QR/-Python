from selenium.webdriver.common.by import By


class CheckoutPage:
    """
    Page Object страницы оформления заказа.
    """

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        """
        :param driver: WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver

    def fill_form(self, first: str, last: str, zip_code: str) -> None:
        """
        Заполняет форму пользователя.

        :param first: имя
        :type first: str
        :param last: фамилия
        :type last: str
        :param zip_code: индекс
        :type zip_code: str
        :return: None
        """
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(zip_code)

    def continue_checkout(self) -> None:
        """
        Переход к следующему шагу.

        :return: None
        """
        self.driver.find_element(*self.CONTINUE).click()

    def get_total(self) -> str:
        """
        Получает итоговую сумму заказа.

        :return: сумма
        :rtype: str
        """
        text = self.driver.find_element(*self.TOTAL).text
        return text.split("$")[1]
