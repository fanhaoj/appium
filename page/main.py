# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
'platformName': 'Android',
'platformVersion': '6.0',
'deviceName': '127.0.0.1:7555',
'appPackage':'com.yckj.eshop',
'appActivity':'com.yckj.eshop.ui.activity.WelcomeActivity',
'noReset': True,
'dontStopAppOnReset': True,
'skipDeviceInitialization': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

def backbutton():
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, 'com.yckj.eshop:id/back')))
    driver.find_element(MobileBy.ID, 'com.yckj.eshop:id/back').click()

def searchspot(send):
    driver.find_element(MobileBy.ID,'com.yckj.eshop:id/searchTv').click()
    driver.find_element(MobileBy.ID,'com.yckj.eshop:id/searchEt').send_keys(send)
    driver.keyevent(66)
    driver.press_keycode(66)

def line_navigation():
    list=driver.find_elements(MobileBy.ID,'com.yckj.eshop:id/image')
    list[0].click()
    backbutton()
    sleep(2)
    list[1].click()
    backbutton()
    sleep(2)
    list[2].click()
    backbutton()
    sleep(2)
    list[3].click()
    backbutton()
    sleep(2)
    list[4].click()
    backbutton()
    #TouchAction(driver).tap(x=104, y=1388).perform()
    driver.quit()

if __name__ == '__main__':
    searchspot('乐华')