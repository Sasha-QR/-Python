from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открыть браузер
driver = webdriver.Chrome()

try:
    # Перейти на страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    wait = WebDriverWait(driver, 10)

    # Ищем кнопку по тексту (стабильный способ)
    blue_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Button with Dynamic ID']")
            )
    )

    # Клик
    blue_button.click()

finally:
    driver.quit()
