from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from base.base_class import Base
import time

class Filtracia_tovara(Base):
    "Класс, содержащий локаторы и методы для фильрации товара."
    # Locators
    eustomi = "//input[@id='wc-block-checkbox-list-option-2']"
    sort_dropdown = "//select[@name='orderby']"
    min_slider = "//span[contains(@class, 'wc-block-formatted-money-amount')][1]"

    # Getters
    def get_input_checkbox(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.eustomi))
        )
        print("Найден чекбокс 'Эустомы'")
        return element

    def get_sort_dropdown(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sort_dropdown))
        )
        print("Найден выпадающий список сортировки")
        return element

    def get_min_slider(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.min_slider))
        )
        min_slider_text = element.text.strip()
        print(f"Минимум слайдера: {min_slider_text}")
        return min_slider_text

    # Actions
    def click_checkbox(self):
        self.get_input_checkbox().click()
        print("Клик по чекбоксу Эустомы")
        time.sleep(1)

    def select_sort_by_price_ascending(self):
        sort_dropdown = self.get_sort_dropdown()
        select = Select(sort_dropdown)
        select.select_by_value("price")
        print("Выбрана сортировка: Цены: по возрастанию")
        time.sleep(2)

    def filtracia_po_checkbox_i_slideru(self):
        self.click_checkbox()
        self.select_sort_by_price_ascending()
        min_price = self.get_min_slider()
        return min_price
