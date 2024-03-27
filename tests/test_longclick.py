from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from page_object.homepage import *
from page_object.longclickpopup import *
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
    
    return driver

@pytest.fixture
def setup():
    driver = init_driver() # precondition
    
    yield driver

    driver.quit() # postcondition

def test_longclick(setup):
    homepage = Homepage(setup)
    longclickpopup = LongClickPopUp(setup)

    homepage.click_longclick_button()
    longclickpopup.input_email(LongClickText.email)
    longclickpopup.click_submit()

    textassertion = longclickpopup.check_popup_longclick()
    
    assert textassertion == 'admin1234@gmail.com'