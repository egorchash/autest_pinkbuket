import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage
from pages.tovar_page import TovarPage
from pages.filtracia_tovara_page import Filtracia_tovara
from pages.dobavlenie_tovara_page import DobavlenieTovaraPage
from pages.buy import but_tovar


def test_vsetovari():
    """Тест перехода покупки товара."""
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
    min_price = ft.filtracia_po_checkbox_i_slideru()
    # Добавление товара
    dt = DobavlenieTovaraPage(driver)
    dt.dobavlenie_tovara(min_price)
    #Покупка товара
    bt = but_tovar(driver)
    bt.pokupka_tovara(min_price)
    print("Автотест по покупке цветов отработал корректно")
    time.sleep(10)
    driver.quit()  # Закрываем драйвер после теста