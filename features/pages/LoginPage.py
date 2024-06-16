from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    login_button = "//li[@class='makeFlex hrtlCenter font10 makeRelative lhUser userLoggedOut']"
    signin_button = "//div[@class='g_id_signin']"
    email_id_click = "//*[@id='identifierId']"
    email_next_button = "//*[@id='identifierNext']/div/button/span"
    password_click = "//*[@id='password']/div[1]/div/div[1]/input"
    password_next_button = "//*[@id='passwordNext']/div/button/span"
    close_login_page = "//span[@class='mybizLoginClose']"

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def click_on_sign_in_button(self):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(EC.visibility_of_element_located((By.XPATH, self.signin_button))).click()
        windowid = self.driver.window_handles
        childwindow = windowid[1]
        self.driver.switch_to.window(childwindow)

    def enter_email_id(self, email_text):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(EC.visibility_of_element_located((By.XPATH, self.email_id_click))).send_keys(email_text)
        self.driver.find_element(By.XPATH, self.email_next_button).click()

    def enter_password(self, password_text):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(EC.visibility_of_element_located((By.XPATH, self.password_click))).send_keys(password_text)
        self.driver.find_element(By.XPATH, self.password_next_button).click()
        windowid = self.driver.window_handles
        childwindow = windowid[0]
        self.driver.switch_to.window(childwindow)

    def close(self):
        WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.visibility_of_element_located((By.XPATH, self.close_login_page))).click()
