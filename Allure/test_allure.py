import allure
from selenium import webdriver
driver = webdriver.Chrome()

@allure.story("Проверки присутствия элементов")
def test_exist_add_to_cart_button():
    with allure.step("Открытие страницы товара"):
        driver.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    with allure.step("Проверка существования на стр. товара кнопки добавления в корзину"):
        add_to_basket_button = driver.find_element("xpath", "//button[contains(@class, 'add-to-basket')]")
        assert add_to_basket_button.is_displayed(), "Отсутствует кнопка добавления в корзину"