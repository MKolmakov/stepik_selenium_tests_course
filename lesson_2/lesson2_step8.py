from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    firs_name = browser.find_element(By.NAME, 'firstname').send_keys('first name')
    last_name = browser.find_element(By.NAME, 'lastname').send_keys('last name')
    email = browser.find_element(By.NAME, 'email').send_keys('mail@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text.txt')  # добавляем к этому пути имя файла
    file_button = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    file_button.send_keys(file_path)

    button_submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
