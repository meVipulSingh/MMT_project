from selenium.webdriver.common.by import By


class DetailPage:
    def __init__(self, driver):
        self.driver = driver
    phone_number_button = "//input[@id='mNo']"

    def i_provide_booking_details(self):
        self.driver.find_element(By.XPATH, "//input[@id='fName']").click()
        self.driver.find_element(By.XPATH, "//input[@id='lName']").click()
        self.driver.find_element(By.XPATH, "//input[@id='email']").click()
        self.driver.find_element(By.XPATH, "//input[@id='mNo']").click()

    def i_enter_phone_number(self, number):
        self.driver.find_element(By.XPATH, self.phone_number_button).send_keys(number)
