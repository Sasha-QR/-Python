from selenium.webdriver.common.by import By


class InventoryPage:
    """
    Page Object страницы товаров.
    """

    def __init__(self, driver):
        """
        :param driver: WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver

    def add_backpack(self) -> None:
        """Добавляет рюкзак в корзину."""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()

    def add_tshirt(self) -> None:
        """Добавляет футболку в корзину."""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

    def add_onesie(self) -> None:
        """Добавляет комбинезон в корзину."""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

    def open_cart(self) -> None:
        """Открывает корзину."""
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
