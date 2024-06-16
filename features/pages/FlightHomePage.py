from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    flight_homepage_url = "https://www.makemytrip.com/flights/"
    round_trip_button = "//*[@data-cy='roundTrip']"
    from_city_click = "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[1]/div[1]/label"
    enter_from_city = "//input[@placeholder='From']"
    from_city_list = "//ul[@role='listbox']/li//p[1]"
    to_city_click = "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[1]/div[2]/label"
    enter_to_city = "//input[@placeholder='To']"
    to_city_list = "//ul[@role='listbox']/li//p[1]"
    travel_month = "//*[@class='DayPicker-Caption'][1]"
    travel_dates = "//div[@class='DayPicker-Month'][1]//p[contains(text(),'')][1]"
    next_month_button = "//span[@aria-label='Next Month']"
    search_button = "//*[@id='top-banner']/div[2]/div/div/div/div[2]/p/a"

    def get_to_the_flight_homepage(self):
        self.driver.get(self.flight_homepage_url)

    def click_on_round_trip(self):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.visibility_of_element_located((By.XPATH, self.round_trip_button))).click()

    def from_city(self, from_city):
        self.driver.find_element(By.XPATH, self.from_city_click).click()
        self.driver.find_element(By.XPATH, self.enter_from_city).send_keys(from_city)
        city = self.driver.find_elements(By.XPATH, self.from_city_list)
        for i in city:
            if i.text == from_city:
                i.click()
                break

    def to_city(self, to_city):
        self.driver.find_element(By.XPATH, self.to_city_click).click()
        self.driver.find_element(By.XPATH, self.enter_to_city).send_keys(to_city)
        city = self.driver.find_elements(By.XPATH, self.to_city_list)
        for i in city:
            if i.text == to_city:
                i.click()
                break

    def departure_and_return_month_date(self, checkin_month, departure_date, return_date):
        while True:
            month = self.driver.find_element(By.XPATH, self.travel_month).text
            if month == checkin_month:

                days = self.driver.find_elements(By.XPATH,self.travel_dates)
                for i in days:
                    if i.text == departure_date:
                        i.click()
                    if i.text == return_date:
                        i.click()
                        break
                break

            else:
                self.driver.find_element(By.XPATH,self.next_month_button).click()

    def click_on_search(self):
        self.driver.find_element(By.XPATH, self.search_button).click()  # search button
