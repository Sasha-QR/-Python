from selenium.webdriver.common.by import By


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first, last, zip_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(zip_code)

    def continue_checkout(self):
        self.driver.find_element(*self.CONTINUE).click()

    def get_total(self):
        text = self.driver.find_element(*self.TOTAL).text
        return text.split("$")[1]
