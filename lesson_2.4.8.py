from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.implicitly_wait(10)

# говорим Selenium проверять в течение 12 секунд, пока цена не станет меньше 100
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button = browser.find_element(By.ID, "book")
button.click()

browser.execute_script("window.scrollBy(0, 150);")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
import math


    # считать значения переменной
x_element = browser.find_element(By.ID,"input_value")
x = int(x_element.text)
y = calc(x)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)


button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve")))
#button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

alert_obj = browser.switch_to.alert
msg = alert_obj.text
print(msg)

