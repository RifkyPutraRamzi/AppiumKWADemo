from appium.webdriver.common.appiumby import AppiumBy
from locators.home_locator import HomeLocator
from selenium.webdriver.common.action_chains import ActionChains 



class Homepage:
    
    def __init__(self,driver):
        self.driver = driver
        
    def click_login_button(self):
        self.driver.find_element(AppiumBy.XPATH,HomeLocator.login_button).click()
    
    def click_autosuggest_button(self):
        self.driver.find_element(AppiumBy.ID,HomeLocator.autosuggest_button).click()
    
    def click_longclick_button(self):
        element = self.driver.find_element(AppiumBy.ID,HomeLocator.longclick_button)
        ta = ActionChains(self.driver)
        ta.click_and_hold(on_element=element)
        ta.perform()

