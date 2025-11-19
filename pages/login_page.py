from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time

class LoginPage(Base):
    """Класс, содержащий локаторы и методы для страницы авторизации."""

    # Locators
    login = "//input[@id='username']"
    password = "//input[@id='password']"
    vhod = "//button[@class='woocommerce-button button woocommerce-form-login__submit']"
    word_login = "//p[contains(., 'Добро пожаловать') and .//strong]"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://pinkbuket.ru/my-account/"

    # Getters
    def get_input_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_vhod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.vhod)))

    def get_main_word(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.word_login))
        )
        print(f"Найден элемент с текстом: {element.text}")
        return element.text

    # Actions
    def input_login(self, user_name):
        self.get_input_login().send_keys(user_name)
        print("Ввод логина")

    def input_password(self, user_password):
        self.get_input_password().send_keys(user_password)
        print("Ввод пароля")

    def click_vhod(self):
        self.get_button_vhod().click()
        print("Клик по кнопке вход")
        time.sleep(1)

    # Methods
    def authorization(self):
        """Авторизация в системе."""
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.input_login("egor.chaschin@yandex.ru")
        self.input_password("Test_1234?")
        self.click_vhod()
        self.assert_word(self.get_main_word(), "Добро пожаловать egor.chaschin")
