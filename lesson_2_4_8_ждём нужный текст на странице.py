from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 12 секунд, пока значение текста элемента не станет $100
    WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID, 'input_value'))
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(20)
    browser.quit()

"""Ситуация: тяжеловесный сайт через впн очень долго грузится, иногда бесконечно долго, соответственно код не выполняется, пока не остановишь загрузку. Но жать вручную на крестик - это отбирать хлеб у роботов. Гуглил, нашел решение в настройках pageLoadStrategy (по умолчанию 'normal', также принимает 'eager' или 'none'). Пример кода:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

link = "example.com"
caps = DesiredCapabilities.CHROME
browser = webdriver.Chrome(desired_capabilities=caps)
caps["pageLoadStrategy"] = "none"
browser.get(link)
# ждем загрузку элемента:
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".example_selector"))) 
# стопаем загрузку сайта:
browser.execute_script("window.stop();")
Для автотестов может и не самая полезная фича, а вот для парсинга - самое то)"""