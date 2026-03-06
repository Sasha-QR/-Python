from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем товары
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

    driver.find_element(
        By.XPATH,
        "//div[text()='Sauce Labs Backpack']"
        "/ancestor::div[@class='inventory_item']"
        "//button"
        ).click()
    driver.find_element(
        By.XPATH,
        "//div[text()='Sauce Labs Bolt T-Shirt']"
        "/ancestor::div[@class='inventory_item']"
        "//button"
        ).click()
    driver.find_element(
        By.XPATH,
        "//div[text()='Sauce Labs Onesie']"
        "/ancestor::div[@class='inventory_item']"
        "//button"
        ).click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    # Заполняем форму
    wait.until(EC.presence_of_element_located((By.ID, "first-name")))

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    # Получаем итоговую сумму
    total_text = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text

    driver.quit()

    assert total_text == "Total: $58.29"
