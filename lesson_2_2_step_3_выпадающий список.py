from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = int(browser.find_element(By.ID, 'num1').text)
    x2 = int(browser.find_element(By.ID, 'num2').text)
    y = str(x1+x2)

    # Выбрать в выпадающем списке значение, равное расчитанной сумме
    Select(browser.find_element(By.TAG_NAME, "select")).select_by_visible_text(y) # варианты методов: select_by_value("значение") (если в коде есть атрибут value) и select.select_by_index(index)

    #Нажать на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()