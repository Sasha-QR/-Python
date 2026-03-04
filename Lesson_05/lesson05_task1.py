from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открыть браузер
driver = webdriver.Chrome()

try:
    # Перейти на страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Явное ожидание появления кнопки
    wait = WebDriverWait(driver, 10)

    # Ищем синюю кнопку по тексту (самый стабильный способ)
    blue_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Blue Button']")
            )
    )

    # Кликнуть
    blue_button.click()

finally:
    # Закрыть браузер
    driver.quit()
