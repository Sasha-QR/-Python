from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack()
    inventory.add_tshirt()
    inventory.add_onesie()

    inventory.open_cart()

    cart.checkout()

    checkout.fill_form("Ivan", "Ivanov", "123456")
    checkout.continue_checkout()

    total = checkout.get_total()

    driver.quit()

    assert total == "58.29"
