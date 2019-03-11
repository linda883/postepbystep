from locators.locators import Locators
class sosoResultPage():

    def __init__(self, driver):
        self.driver = driver
        '''
        driver: webdriver
        '''

        self.ss_text_xpath = Locators.ss_text_xpath_loc

    def get_sstext(self):
        return self.driver.find_element(*self.ss_text_xpath).text

