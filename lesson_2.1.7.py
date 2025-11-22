from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
import math


    # считать значения переменной
x_element = browser.find_element(By.ID,"treasure")
x_valuex=x_element.get_attribute("valuex")
x = int(x_valuex)
y = calc(x)

    # заполнить поля
input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)
    #нажать чек-бокс
option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()
    #выбрать радиобаттон
option2 = browser.find_element(By.ID, "robotsRule")
option2.click()
 
    # Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()