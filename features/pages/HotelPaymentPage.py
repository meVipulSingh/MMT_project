from selenium.webdriver.common.by import By


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
    pay_now_button = "//a[normalize-space()='Pay Now']"

    def i_click_on_pay_now(self):
        self.driver.find_element(By.XPATH, self.pay_now_button).click()

