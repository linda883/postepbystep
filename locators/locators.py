
from selenium import webdriver
from selenium.webdriver.common.by import By

class Locators():

    # sosopage object
    sousuo_textbox_id_loc = (By.ID, "kw")
    baiduyixia_button_id_loc = (By.ID, "su")
    print(sousuo_textbox_id_loc)
    print(baiduyixia_button_id_loc)
    # 变量返回的是元组类型('id', 'kw')

    # sosoresultpage object
    ss_text_xpath_loc = (By.XPATH, "//*[@id='1']")
    print(ss_text_xpath_loc)
