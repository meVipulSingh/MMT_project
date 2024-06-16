import time
from selenium import webdriver


# Hook Methods
def before_scenario(context, driver):
    context.options = webdriver.ChromeOptions()
    context.options.add_experimental_option('detach', True)
    context.driver = webdriver.Chrome(options=context.options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)


def after_scenario(context, driver):
    time.sleep(10)
    context.driver.quit()
