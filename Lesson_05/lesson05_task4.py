from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открыть Firefox
driver = webdriver.Firefox()

try:
    # Перейти на страницу логина
    driver.get("http://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)

    # Найти поле username и ввести логин
    username = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username.send_keys("tomsmith")

    # Найти поле password и ввести пароль
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    # Нажать кнопку Login
    login_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
        )
    login_button.click()

    # Дождаться появления зеленой плашки
    success_message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    # Вывести текст в консоль
    print(success_message.text)

finally:
    # Закрыть браузер
    driver.quit()
