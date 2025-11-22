from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.NAME, 'firstname')
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, 'lastname')
input2.send_keys("Petrov")
input3 = browser.find_element(By.NAME, 'email')
input3.send_keys("Email")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'lesson_2.2.8.txt')           # добавляем к этому пути имя файла 
browser.find_element(By.ID, "file").send_keys(file_path)

    # Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()