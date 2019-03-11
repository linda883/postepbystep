# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from page.Soso_Page import SosoPage
from page.soso_result_page import sosoResultPage
import time


class AppDynamicsJob(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(
            executable_path='/Users/lindafang/PycharmProjects/postepbystep/testcases/chromedriver')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.base_url = ""
        cls.verificationErrors = []

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://www.baidu.com/")

        sobd = SosoPage(driver)
        sobd.enter_sousuotext("selenium")
        time.sleep(1)
        so_result = sosoResultPage(driver)
        text = so_result.get_sstext()
        print(text)
        assert 'selenium' in text
        time.sleep(1)



    @classmethod
    def tearDownClass(cls):
        print('\ntest complete!')
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
