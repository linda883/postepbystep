from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='/Users/lindafang/PycharmProjects/postepbystep/easystart/chromedriver')
driver.implicitly_wait(30)
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").click()
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(1)
print(driver.title)

assert "selenium" in driver.title
driver.close()
driver.quit()

