from appium.webdriver.common.appiumby import AppiumBy
from locators.admin_locator import AdminLocator

class AdminPage:
    def __init__(self,driver):
        self.driver = driver
        
    def check_admin_title_text(self):
        text = self.driver.find_element(AppiumBy.XPATH,AdminLocator.text_enter_admin).text
        
        return text
    
    def check_wrong_login(self):
        wrongtext = self.driver.find_element(AppiumBy.ID,AdminLocator.text_wrong_login).text

        return wrongtext