from appium.webdriver.common.appiumby import AppiumBy
from locators.autosuggest_locator import AutosuggestLocator

class AutoSuggestPage:
    def __init__(self,driver):
        self.driver = driver
        
    def input_text(self,text):
        self.driver.find_element(AppiumBy.ID,AutosuggestLocator.input_text).send_keys(text)
               
    def click_submit(self):
        self.driver.find_element(AppiumBy.ID,AutosuggestLocator.submit_button).click()

    def check_text_suggest(self):
        textassert = self.driver.find_element(AppiumBy.ID,AutosuggestLocator.text_assert).text
        
        return textassert