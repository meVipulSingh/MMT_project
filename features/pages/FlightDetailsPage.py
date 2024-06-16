from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class DetailsPage:
    def __init__(self, driver):
        self.driver = driver

        windowid = self.driver.window_handles
        childwindow = windowid[1]
        self.driver.switch_to.window(childwindow)

    add_new_adult_button = "//button[normalize-space()='+ ADD NEW ADULT']"
    first_name_button = "//input[@placeholder='First & Middle Name']"
    last_name_button = "//input[@placeholder='Last Name']"
    gender_selection_button = "//*[@id='wrapper_ADULT']/div[3]/div[2]/div[2]/div/div/div[1]/div[3]/div/div/label[1]"
    phone_number_button = "//*[@id='Mobile No']/div/input"
    continue_button = "//*[@id='mainSection_0']/div[2]/button"

    def adding_passenger_details(self):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.element_to_be_clickable((By.XPATH, self.add_new_adult_button))).click()

    def first_name(self, f_name):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.visibility_of_element_located((By.XPATH, self.first_name_button))).send_keys(f_name)

    def last_name(self, l_name):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.visibility_of_element_located((By.XPATH, self.last_name_button))).send_keys(l_name)

    def gender_selection(self):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.visibility_of_element_located((By.XPATH, self.gender_selection_button))).click()

    def enter_phone_number(self, number):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.visibility_of_element_located((By.XPATH, self.phone_number_button))).send_keys(number)

    def click_to_continue(self):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.visibility_of_element_located((By.XPATH, self.continue_button))).click()
