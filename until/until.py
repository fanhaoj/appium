# -*- coding: utf-8 -*-
from appium.webdriver import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Until:
    def backbutton(self):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, 'com.yckj.eshop:id/back')))
        driver.find_element(By.ID, 'com.yckj.eshop:id/back').click()