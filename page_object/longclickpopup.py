from appium.webdriver.common.appiumby import AppiumBy
from locators.longclick_locator import LongClickLocator

class LongClickPopUp:
    def __init__(self,driver):
        self.driver = driver
        
    def input_email(self,email):
        self.driver.find_element(AppiumBy.ID,LongClickLocator.input_email).send_keys(email)
        
    def click_submit(self):
        self.driver.find_element(AppiumBy.ID,LongClickLocator.submit_button).click()

    def check_popup_longclick(self):
        textassertion = self.driver.find_element(AppiumBy.XPATH,LongClickLocator.toast_text).text
        
        return textassertion