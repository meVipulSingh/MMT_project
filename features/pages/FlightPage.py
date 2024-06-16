from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class FlightPage:
    def __init__(self, driver):
        self.driver = driver

    add_handle_button = "//*[@id='root']/div/div[2]/div[2]/div[2]/div/span"
    flight_selection_button = "//button[@class='splitFooterButton button buttonPrimary buttonBig appendBottom8 ']"
    continue_button = "//*[@id='listing-id']/div[2]/div[1]/ul/li[2]"
    try_book_now_button = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/button"
    else_book_now_button = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[3]/button"

    def add_handle(self):
        try:
            WebDriverWait(self.driver, 20, poll_frequency=2).until(EC.visibility_of_element_located(
                (By.XPATH, self.add_handle_button))).click()  # AAd Handle
        except:
            self.driver.find_element(By.XPATH, self.add_handle_button).click()

    def flights_selection_from_departure_city_to_return_city(self):
        self.driver.find_element(By.XPATH, self.flight_selection_button).click()

    def book_now(self):
        try:
            self.driver.find_element(By.XPATH, self.continue_button).click()
            self.driver.find_element(By.XPATH, self.try_book_now_button).click()
        except:
            self.driver.find_element(By.XPATH, self.else_book_now_button).click()


