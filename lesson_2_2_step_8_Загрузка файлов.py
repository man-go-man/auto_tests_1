from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    # Заполнить текстовые поля: имя, фамилия, email
    browser.find_element(By.NAME, "firstname").send_keys('Leopold')
    browser.find_element(By.NAME, "lastname").send_keys('Second')
    browser.find_element(By.NAME, "email").send_keys('L2@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'my_test_file.txt')  # добавляем к этому пути имя файла, который нужно прикрепить на web-странице (он по умолчанию лежит в папке исполняемого файла питон)
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path) # крепим файл
    """ Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут type="file". 
    Мы должны сначала найти этот элемент с помощью селектора, а затем применить к нему метод send_keys(file_path)."""
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(10)
    browser.quit()
