class Base:
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver):
        self.driver = driver

    def assert_word(self, word, result):
        """Проверка значения текста"""
        value_word = word
        assert value_word == result, f"Ожидаемый текст: {result}, найденный текст: {value_word}"
        print("Значение текста верно")

