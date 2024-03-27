from appium.webdriver.common.appiumby import AppiumBy
from locators.login_locator import LoginLocator

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        
    def input_username(self,username):
        self.driver.find_element(AppiumBy.ID,LoginLocator.input_username).send_keys(username)
        
    def input_password(self,password):
        self.driver.find_element(AppiumBy.ID,LoginLocator.input_password).send_keys(password)
        
    def click_submit(self):
        self.driver.find_element(AppiumBy.ID,LoginLocator.submit_button).click()
