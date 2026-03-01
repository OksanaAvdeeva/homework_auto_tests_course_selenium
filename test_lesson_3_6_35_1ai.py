import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1?auth=login"
    browser.implicitly_wait(3)
    browser.get(link)
#try:
    time.sleep(5)
    input1 = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
    input1.send_keys('Mishunina-Ok@yandex.ru')
    input2 = browser.find_element(By.XPATH, '//*[@id="id_login_password"]')
    input2.send_keys('00800081')
    button = browser.find_element(By.XPATH, '//*[@id="login_form"]/button')
    button.click()
#finally:
    time.sleep(5)

    print("✍️ Ждем поле ответа...")
    answer_field = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea"))
    )
    
    # ПРОВЕРЯЕМ ПУСТОЕ ПОЛЕ
    assert answer_field.get_attribute("value") == "", "Поле НЕ пустое!"
    print("✅ Поле пустое")
    
    # 4. ТЕПЕРЬ вычисляем и вводим ПРАВИЛЬНЫЙ ОТВЕТ
    print("🧮 Вычисляем ответ...")
    correct_answer = str(math.log(int(time.time())))
    answer_field.send_keys(correct_answer)
    print(f"Ввели: {correct_answer}")
    
    # 5. КНОПКА ОТПРАВИТЬ (теперь активна!)
    print("📤 Отправляем...")
    submit_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    submit_btn.click()
    
    # 6. ПРОВЕРЯЕМ "Correct!"
    print("✅ Ждем 'Correct!'...")
    feedback = WebDriverWait(browser, 10).until(
        EC.any_of(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".smart-hints__hint"), "Correct!"),
            EC.text_to_be_present_in_element((By.CLASS_NAME, "hint"), "Correct!")
        )
    )
    print("🎉 Correct! Получено!")



#https://stepik.org/lesson/236895/step/1
#https://stepik.org/lesson/236896/step/1
#https://stepik.org/lesson/236897/step/1
#https://stepik.org/lesson/236898/step/1
#https://stepik.org/lesson/236899/step/1
#https://stepik.org/lesson/236903/step/1
#https://stepik.org/lesson/236904/step/1
#https://stepik.org/lesson/236905/step/1

