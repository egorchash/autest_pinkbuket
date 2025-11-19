from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
import time

class DobavlenieTovaraPage(Base):
    "Класс, содержащий локаторы и методы для добавления товара в корзину."
    # Locators
    item_prices = "//span[contains(@class, 'woocommerce-Price-amount')]"
    buy_button = ".//*[contains(@class, 'add_to_cart_button') or contains(@class, 'ajax_add_to_cart') or contains(@type, 'submit')]"
    poditog = "//p[contains(@class, 'woocommerce-mini-cart__total') and contains(., 'Подытог')]//span[contains(@class, 'woocommerce-Price-amount')]"

    # Getters and Actions
    def find_and_click_buy_button_by_price(self, price):
        try:
            formatted_price = price.replace(" ", "").replace("₽", "").strip()
            print(f"Ищем товар с ценой: {formatted_price}")

            price_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.item_prices))
            )

            target_element = None
            for element in price_elements:
                element_price_text = element.text
                element_price = element_price_text.replace(" ", "").replace("₽", "").strip()
                print(f"Проверяем цену: {element_price}")
                if element_price == formatted_price:
                    target_element = element.find_element(By.XPATH, "./ancestor::div[contains(@class, 'shop-item')]")
                    print(f"Найден товар с ценой: {element_price}")
                    break

            if not target_element:
                raise Exception(f"Товар с ценой {price} не найден")

            action = ActionChains(self.driver)
            action.move_to_element(target_element).perform()
            time.sleep(2)

            buy_button = target_element.find_element(By.CSS_SELECTOR,
                                                     "button[type='submit'], a.add_to_cart_button, button.single_add_to_cart_button")
            buy_button.click()
            print(f"Успешно кликнули по кнопке 'Купить' для товара с ценой: {formatted_price}")
            return formatted_price

        except Exception as e:
            print(f"Ошибка при наведении и клике на кнопку 'Купить' для товара с ценой '{price}': {e}")
            raise

    def get_poditog(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.poditog))
        )
        element_poditog = element.text
        formatted_price_poditog = element_poditog.replace(" ", "").replace("₽", "").strip()
        print(f"Найден элемент с текстом: {formatted_price_poditog}")
        return formatted_price_poditog


    def dobavlenie_tovara(self, price):
        self.find_and_click_buy_button_by_price(price) # добавляем товар в корзину
        formatted_price = price.replace(" ", "").replace("₽", "").strip()
        time.sleep(1)
        self.assert_word(formatted_price, self.get_poditog())
        return formatted_price
        time.sleep(3)

