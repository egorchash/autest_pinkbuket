from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class TovarPage(Base):
    "Класс, содержащий локаторы и методы для страницы все товары."
    # Locators
    vse_tovari = "//a[contains(text(), 'Все товары')]"
    buket_cvet_podar = "//h1[contains(text(), 'Букеты цветы подарки')]"

    # Getters
    def get_input_vsetovari(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.vse_tovari))
        )
        print("Найдена кнопка 'Все товары'")
        return element

    def get_buket_cvet_podar(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.buket_cvet_podar))
        )
        print(f"Найден элемент с текстом: {element.text}")
        return element.text

    def click_vsetovari(self):
        self.get_input_vsetovari().click()
        print("Клик по кнопке 'Все товары'")

    def vhod_vse_tovari(self):
        self.click_vsetovari()
        self.assert_word(self.get_buket_cvet_podar(), "Букеты цветы подарки")
