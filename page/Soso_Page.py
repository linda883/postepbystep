from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from locators.locators import Locators


class SosoPage(object):

    def __init__(self, driver):
        self.driver: WebDriver = driver

        self.sousuo_textbox_id = (By.ID, 'kw')
        self.baiduyixia_button_id = (By.ID, "su")

    def enter_sousuotext(self, soso_text):
        self.driver.find_element(*self.sousuo_textbox_id).click()
        self.driver.find_element(*self.sousuo_textbox_id).clear()
        self.driver.find_element(*self.sousuo_textbox_id).send_keys(soso_text)

    def click_baiduyixiao(self):
        self.driver.find_element(*self.baiduyixia_button_id).click()
