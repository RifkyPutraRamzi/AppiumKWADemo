from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from page_object.homepage import *
from page_object.loginpage import *
from page_object.adminpage import *
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
    
def test_login_positive(setup):
    homepage = Homepage(setup)
    loginpage = LoginPage(setup)
    adminpage = AdminPage(setup)
    
    homepage.click_login_button()
    loginpage.input_username(LoginData.username)
    loginpage.input_password(LoginData.password)
    loginpage.click_submit()
    
    text = adminpage.check_admin_title_text()
    
    assert text == 'Enter Admin'

def test_login_negative(setup):
    homepage = Homepage(setup)
    loginpage = LoginPage(setup)
    adminpage = AdminPage(setup)
    
    homepage.click_login_button()
    loginpage.input_username(WrongData.username)
    loginpage.input_password(WrongData.password)
    loginpage.click_submit()
    
    text = adminpage.check_wrong_login()
    
    assert text == 'Wrong Credentials'