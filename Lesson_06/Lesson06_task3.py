from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Запуск браузера (Chrome)
driver = webdriver.Chrome()

try:
    # 1. Переход на сайт
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
        )

    wait = WebDriverWait(driver, 20)

    # 2. Ожидание загрузки всех картинок
    # Ждём, пока у третьей картинки атрибут src перестанет быть пустым
    third_image = wait.until(
        lambda d: (
            imgs := d.find_elements(By.TAG_NAME, "img")
        ) and len(imgs) >= 3 and imgs[2].get_attribute("src")
    )

    # 3. Получение значения атрибута src у 3-й картинки
    images = driver.find_elements(By.TAG_NAME, "img")
    third_image_src = images[2].get_attribute("src")

    # 4. Вывод в консоль
    print(third_image_src)

finally:
    driver.quit()
