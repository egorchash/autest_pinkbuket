from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
import re
import time


class but_tovar (Base):
    "Класс, содержащий локаторы и методы для покупки."
    # Locators
    ovormlenie = "//a[@class= 'button wc-forward']"
    itog = "//td[@class='product-total']//span[@class = 'woocommerce-Price-amount amount']"
    name_phone = "//input[@name = 'billing_phone']"
    zakaz = "//button[@class = 'button alt']"
    cena_itog = "//span[contains(@class, 'ng-star-inserted') and contains(text(), '₽')]"


    #Getters
    def get_ovormlenie(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ovormlenie)))

    def get_itog(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.itog))
        )
        element_poditog = element.text
        formatted_price_itog = element_poditog.replace(" ", "").replace("₽", "").strip()
        print(f"Найден элемент с текстом: {formatted_price_itog}")
        return formatted_price_itog

    def get_name_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_phone)))

    def get_zakaz(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zakaz)))


    def get_cena_itog(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cena_itog))
        )
        price_itogo = element.text
        numbers_only = re.sub(r'\D', '', price_itogo)
        print(numbers_only)
        return numbers_only

    #Action

    def click_ovormlenie(self):
        self.get_ovormlenie().click()
        print("Клик по кнопке оформление")
        time.sleep(1)

    def input_phone(self, user_phone):
        self.get_name_phone().send_keys(user_phone)
        print("Ввод телефона")

    def click_zakaz(self):
        self.get_zakaz().click()
        print("Клик по кнопке Подтвердить заказ")

    def pokupka_tovara(self, price):
        self.click_ovormlenie()
        formatted_price = price.replace(" ", "").replace("₽", "").strip()
        self.assert_word(formatted_price, self.get_itog())
        itog_value = self.get_itog()
        print(f"Минимальная цена: {formatted_price}")
        print(f"Цена при покупке итого: {itog_value}")
        self.input_phone("9999999999")
        self.click_zakaz()
        self.assert_word(itog_value,self.get_cena_itog())







