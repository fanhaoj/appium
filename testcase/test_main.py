# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium_flutter_finder.flutter_finder import FlutterFinder
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_main:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.yckj.eshop',
            'appActivity': 'com.yckj.eshop.ui.activity.WelcomeActivity',
            'noReset': True,
            'dontStopAppOnReset': True,
            'skipDeviceInitialization': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
        self.finder=FlutterFinder()

    def teardown(self):
        self.driver.quit()

    def test_order(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((MobileBy.XPATH,'//*[@text="景区门票"]')))
        self.driver.find_element(MobileBy.XPATH,'//*[@text="目的地"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="渭南"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="华山风景名胜区"]').click()
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("").instance(0))')
        # self.driver.find_element(MobileBy.XPATH,'//android.view.View[@content-desc="购买"])[4]').click()
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID,'门票')))
        actions=TouchAction(self.driver)
        actions.press(x=348,y=1132).wait(1000).move_to(x=348,y=322).wait(1000).release().perform()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((MobileBy.XPATH, '(//android.view.View[@content-desc="购买"])[3]')))
        self.driver.find_element(MobileBy.XPATH,'(//android.view.View[@content-desc="购买"])[3]').click()
        #下单
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.yckj.eshop:id/tvOperatingLess"]').click()


