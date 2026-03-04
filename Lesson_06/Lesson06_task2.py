from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера (Chrome)
driver = webdriver.Chrome()

try:
    # 1. Переход на сайт
    driver.get("http://uitestingplayground.com/textinput")

    wait = WebDriverWait(driver, 10)

    # 2. Ввод текста SkyPro в поле
    input_field = wait.until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("SkyPro")

    # 3. Нажатие на синюю кнопку
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # 4. Получение текста кнопки
    updated_button = wait.until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    # Получаем текст кнопки
    button_text = driver.find_element(By.ID, "updatingButton").text

    # 5. Вывод в консоль
    print(button_text)

finally:
    driver.quit()
