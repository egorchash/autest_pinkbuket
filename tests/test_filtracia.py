from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage
from pages.tovar_page import TovarPage
from pages.filtracia_tovara_page import Filtracia_tovara

def test_vsetovari():
    """Тест перехода на страницу 'Все товары'."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start 'Все товары' Test")

    # Авторизация
    lp = LoginPage(driver)
    lp.authorization()

    # Переход на страницу всех товаров
    tp = TovarPage(driver)
    tp.vhod_vse_tovari()

    # Фильтрация
    ft = Filtracia_tovara(driver)
    ft.filtracia_po_checkbox_i_slideru()

    driver.quit()  # Закрываем драйвер после теста

