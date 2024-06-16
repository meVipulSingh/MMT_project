from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    review_detail_button = "//*[@id='root']/div/div[2]/div[4]/div/div[2]/button"
    yes_please_button = "//button[normalize-space()='Yes, Please']"
    skip_to_add_ons_button = "//span[@class='linkText']"
    proceed_to_pay_button = "//button[normalize-space()='Proceed to pay']"

    def review_details(self):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.visibility_of_element_located((By.XPATH, self.review_detail_button))).click()

    def yes_please(self):
        element = WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.element_to_be_clickable((By.XPATH, self.yes_please_button)))
        self.driver.execute_script("arguments[0].click()", element)

    def skip_to_add_ons(self):
        element = WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.element_to_be_clickable((By.XPATH, self.skip_to_add_ons_button)))
        self.driver.execute_script("arguments[0].click()", element)

    def proceed_to_pay(self):
        element = WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.element_to_be_clickable((By.XPATH, self.proceed_to_pay_button)))
        self.driver.execute_script("arguments[0].click()", element)
