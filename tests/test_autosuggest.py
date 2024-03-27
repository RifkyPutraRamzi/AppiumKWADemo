from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from page_object.homepage import *
from page_object.autosuggestpage import *
from data.data_io import *

import pytest

def init_driver():
    options = UiAutomator2Options()

    options.udid = '127.0.0.1:62001'
    options.platform_name = 'Android'
    options.app_package = 'com.code2lead.kwad'
    options.app_activity = 'com.code2lead.kwad.MainActivity'

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(811, 1505)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(817, 260)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    
    return driver

@pytest.fixture
def setup():
    driver = init_driver() # precondition
    
    yield driver

    driver.quit() # postcondition

def test_autosuggest(setup):
    homepage = Homepage(setup)
    autosuggestpage = AutoSuggestPage(setup)
    
    homepage.click_autosuggest_button()
    autosuggestpage.input_text(AutoSuggestText.text)
    autosuggestpage.click_submit()

    textassert = autosuggestpage.check_text_suggest()

    assert textassert == 'Testing Automation Android'
