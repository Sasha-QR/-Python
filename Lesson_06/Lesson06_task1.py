from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # 1. Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # 2. Нажатие на синюю кнопку
    button = driver.find_element(By.ID, "ajaxButton")
    button.click()

    # 3. Ожидание появления зелёной плашки
    wait = WebDriverWait(driver, 20)
    green_text = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )

    # 4. Получение текста
    result_text = green_text.text

    # 5. Вывод в консоль
    print(result_text)
finally:
    driver.quit()
