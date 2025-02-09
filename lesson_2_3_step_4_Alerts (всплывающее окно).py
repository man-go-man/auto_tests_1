from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(10)
    browser.quit()