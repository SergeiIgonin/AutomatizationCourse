"""Пример структуры base_page"""
from selenium.webdriver.chrome.webdriver import WebDriver  # аннотация драйвера для дальнейшего автозаполнения его методов


# или так: from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:  # создаем родительский класс для всех страниц

    # 1. Общие локаторы, доступные для всех pages (являются статическими атрибутами класса)
    LOGOUT_BUTTON = ("xpath", "//button[@id='logout']")
    LOGO_LINK = ("xpath", "//a[@id='logo']")

    # 2. Конструктор по инициализации атрибутов объектов класса (драйвер, wait и т.д.), доступного для всех pages
    def __init__(self, driver):
        self.driver: WebDriver = driver  # добавляем ": WebDriver" чтобы Pycharm понимал, что объект driver это объект класса WebDriver
        ...

    # 3. Общие методы действий, доступные всем pages (вместо self везде будет подставляться объект конкретной page из файла с тестами)
    def open(self):  # метод открытия любой страницы
        self.driver.get(self.PAGE_URL)  # при запуске кода и иниц. объекта страницы локатор PAGE_URL начнет существовать

    def click_logout_button(self):  # метод нажатия кнопки "Logout"
        self.driver.find_element(*self.LOGOUT_BUTTON).click()  # (?) будет ли работать без распаковщика и self в скобках?

    # ...

# (!) ВАЖНЫЕ правила при написании методов-шагов в любых пейджах:

# 1. Используем EC, если планируем взаимодействовать с элементом методами send_keys/click и т.п, например:
# self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD2)).send_keys(password)
# self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
#
# 2. Используем find_element, если нужно просто найти элемент для ассерта, например:
# cart_message = self.driver.find_element(*self.CART_MSG)
#         assert "корзина пуста" or "basket is empty" in cart_message.text, "Корзина не пуста"
