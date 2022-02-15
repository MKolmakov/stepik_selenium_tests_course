from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    value_x = browser.find_element(By.ID, "input_value")
    x = value_x.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    text_field = browser.find_element(By.ID, "answer").send_keys(y)
    checkbox_robot = browser.find_element(By.ID, "robotCheckbox").click()
    radiobutton_robot = browser.find_element(By.ID, "robotsRule").click()
    button_submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
    