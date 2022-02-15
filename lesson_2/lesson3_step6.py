from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, 'trollface.btn').click()

    # Переключаемся на другую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    text_field = browser.find_element(By.CLASS_NAME, "form-control").send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


finally:
    print(browser.switch_to.alert.text)
    browser.quit()
