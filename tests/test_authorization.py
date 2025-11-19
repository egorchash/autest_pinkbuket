from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage

def test_auth():
    """Тест авторизации."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start Authorization Test")

    lp = LoginPage(driver)
    lp.authorization()

    driver.quit()  # Закрываем драйвер после теста
