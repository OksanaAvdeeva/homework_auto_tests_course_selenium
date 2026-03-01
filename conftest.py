import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    service = Service(ChromeDriverManager().install())
    _browser = webdriver.Chrome(service=service)
    _browser.maximize_window()
    yield _browser
    _browser.quit()
    print("browser closed")