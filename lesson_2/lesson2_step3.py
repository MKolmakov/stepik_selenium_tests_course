from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#def calc(num1, num2):
    #return str(num1 + num2)

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #find_num1 = browser.find_element(By.ID, "num1")
    #num1 = int(find_num1.text)
    #find_num2 = browser.find_element(By.ID, "num2")
    #num2 = int(find_num2.text)
    #total = calc(num1, num2)

    total = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(total))

    button = browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()

# except Exception as error:
#     print(f'Произошла ошибка, вот её трэйсбэк: {error}')

