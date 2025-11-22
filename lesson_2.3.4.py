from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

    # Жмем кнопку
button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
button.click()

#согласиться с алертом
confirm = browser.switch_to.alert
confirm.accept()

link = "https://suninjuly.github.io/alert_redirect.html?"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
import math

    # считать значения переменной
x_element = browser.find_element(By.ID,"input_value")
x = int(x_element.text)
y = calc(x)

    # заполнить поля
input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)

    # Жмем кнопку
button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
button.click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()


