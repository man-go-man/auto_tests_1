from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    y = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID, 'robotsRule'))
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(10)
    browser.quit()
