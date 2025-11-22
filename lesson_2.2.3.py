
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

import math

def calc(sum):
    return (x+y)


    # считать значения переменной
x_text = browser.find_element(By.ID,"num1")
x = int(x_text.text)
y_text = browser.find_element(By.ID,"num2")
y = int(y_text.text)
s = calc(sum)
s=str(s)

browser.find_element(By.CSS_SELECTOR, (f"[value='{s}']")).click()

 
    # Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()