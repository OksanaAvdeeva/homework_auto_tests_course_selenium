from selenium import webdriver
browser = webdriver.Chrome()
import time
# или browser.execute_script("alert('Robots at work');")

#или browser.execute_script("document.title='Script executing';")
browser.execute_script("document.title='Script executing';alert('Robots at work');")

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()