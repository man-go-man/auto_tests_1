"""Переход на новую вкладку браузера
При работе с веб-приложениями приходится переходить по ссылкам, которые открываются в новой вкладке браузера.
WebDriver может работать только с одной вкладкой браузера. При открытии новой вкладки WebDriver продолжит работать
со старой вкладкой. Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
Это делается с помощью команды switch_to.window:

browser.switch_to.window(window_name)
Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

new_window = browser.window_handles[1]
Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

first_window = browser.window_handles[0]
После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import pyperclip as pc # возможность копирования в буфер обмена

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()
    pc.copy(browser.switch_to.alert.text.split(': ')[-1])  # сохранить число в конце текста алерта в буфер для самостоятельной вставки в ответ курса
finally:
    time.sleep(10)
    browser.quit()