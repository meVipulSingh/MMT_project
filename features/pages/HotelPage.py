from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HotelPage:
    def __init__(self, driver):
        self.driver = driver

    hotel_search_button = "//input[@placeholder='Search for locality / hotel name']"
    hotel_drop_down_button = "//ul[@role='listbox']/li/a/p/span[2]"
    hotel_selection_button = "(//*[@id='Listing_hotel_0'])[1]"
    book_this_now_button = "//button[@id='detpg_headerright_book_now']"

    def searching_for_good_hotel(self, hotel):
        self.driver.find_element(By.XPATH, self.hotel_search_button).send_keys(hotel)

    def selecting_hotel_i_searched_for(self):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.visibility_of_element_located((By.XPATH, self.hotel_drop_down_button))).click()
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.element_to_be_clickable((By.XPATH, self.hotel_selection_button))).click()

        windowid = self.driver.window_handles
        childwindow = windowid[1]
        self.driver.switch_to.window(childwindow)

    def booking_the_hotel(self):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.visibility_of_element_located((By.XPATH, self.book_this_now_button))).click()
