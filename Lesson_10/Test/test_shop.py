import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Shop")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Проверка оформления заказа")
@allure.description("Проверка итоговой суммы заказа")
def test_shop():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step("Открыть сайт и авторизоваться"):
        login.open()
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары"):
        inventory.add_backpack()
        inventory.add_tshirt()
        inventory.add_onesie()

    with allure.step("Открыть корзину"):
        inventory.open_cart()

    with allure.step("Перейти к оформлению"):
        cart.checkout()

    with allure.step("Заполнить форму"):
        checkout.fill_form("Ivan", "Ivanov", "123456")
        checkout.continue_checkout()

    with allure.step("Получить итоговую сумму"):
        total = checkout.get_total()

    with allure.step("Проверка суммы"):
        assert total == "58.29"

    driver.quit()    
