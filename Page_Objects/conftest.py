import pytest                       # для работы с фикстурами
from selenium import webdriver


@pytest.fixture(autouse=True)       # фикстура будет автоматически использована каждым тестовым методом
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()
