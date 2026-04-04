from selenium.webdriver.common.by import By


class CartPage:
    """
    Page Object для корзины.
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        """
        :param driver: WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver

    def checkout(self) -> None:
        """
        Переход к оформлению заказа.

        :return: None
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
