from selenium.webdriver.common.by import By


class LoginPage:
    """
    Page Object страницы логина.
    """

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        """
        :param driver: WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открывает страницу логина.

        :return: None
        """
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход.

        :param username: логин
        :type username: str
        :param password: пароль
        :type password: str
        :return: None
        """
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
