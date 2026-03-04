from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открыть браузер Firefox
driver = webdriver.Firefox()

try:
    # Перейти на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    wait = WebDriverWait(driver, 10)

    # Найти поле ввода (на странице только один input)
    input_field = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )

    # Ввести Sky
    input_field.send_keys("Sky")

    # Очистить поле
    input_field.clear()

    # Ввести Pro
    input_field.send_keys("Pro")

finally:
    # Закрыть браузер
    driver.quit()
