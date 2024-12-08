"""Пример структуры *_page"""

from Page_Objects.pages.base_page import BasePage  # импортируем родительский класс BasePage


class LoginPage(BasePage):  # создаем класс для конкретной страницы (наследование от BasePage)

    # 1. URL страницы (является статическим атрибутом класса)
    PAGE_URL = "https://example.com"

    # 2. Локаторы этой страницы (являются статическими атрибутами класса)
    LOGIN_FIELD = ("xpath", "//input[@id='login']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON = ("xpath", "//input[@id='logout']")

    # 3. Методы действий только для этой страницы (вместо self везде будет подставляться объект конкретной page из файла с тестами)
    def enter_login(self, login):  # в параметре укажем переменная login, которую определим в тестовом методе файла tests
        self.driver.find_element(*self.LOGIN_FIELD).send_keys(login)  # в аргументе также укажем переменную login из тестового метода

    def enter_password(self):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys("123123123")

    def click_on_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
