from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    hotel_url = "https://www.makemytrip.com/hotels/"
    city_drop_down_button = "//input[@id='city']"
    city_send_keys_button = "//input[@placeholder='Where do you want to stay?']"
    city_list_button = "(//ul[@role='listbox'])[1]/li"
    month_button = "//*[@class='DayPicker-Caption'][1]"
    days_button = "(//div[@class='DayPicker-Body'])[1]//div[@class='DayPicker-Week']//div[contains(text(),'')]"
    next_month_click_button = "//span[@aria-label='Next Month']"
    adults_drop_down_button = "(//*[@class='gstSlct'])[2]"
    adult_selection_button = "//li[normalize-space()='01']"
    apply_button = "//button[normalize-space()='Apply']"
    search_button = "//button[@id='hsw_search_button']"

    def get_to_hotel_home_page(self):
        self.driver.get(self.hotel_url)

    def click_on_city_drop_down(self):
        self.driver.find_element(By.XPATH, self.city_drop_down_button).click()

    def selecting_city_from_drop_down(self, city):
        self.driver.find_element(By.XPATH, self.city_send_keys_button).send_keys(city)
        cities = self.driver.find_elements(By.XPATH, self.city_list_button)
        for i in cities:
            if i.text == city:
                i.click()
                break

    def checkin_and_checkout_month_and_date(self, checkin_month, checkin_date, checkout_date):
        while True:
            month = self.driver.find_element(By.XPATH, self.month_button).text
            if month == checkin_month:

                days = self.driver.find_elements(By.XPATH, self.days_button)
                for i in days:
                    if i.text == checkin_date:
                        i.click()
                    if i.text == checkout_date:
                        i.click()
                        break
                break

            else:
                self.driver.find_element(By.XPATH, self.next_month_click_button).click()

    def selecting_guests(self):
        self.driver.find_element(By.XPATH, self.adults_drop_down_button).click()
        self.driver.find_element(By.XPATH, self.adult_selection_button).click()
        self.driver.find_element(By.XPATH, self.apply_button).click()

    def clicking_on_search(self):
        self.driver.find_element(By.XPATH, self.search_button).click()
