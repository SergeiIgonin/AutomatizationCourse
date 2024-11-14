"""Класс Scrolls импортируем и вызываем его методы для скролла экрана"""

class Scrolls:

    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    def scroll_by(self, x, y):                                      # Скролл по осям X и Y
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):                                     # Скролл в самый низ страницы
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):                                        # Скролл в самый верх страницы
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, element):                           # Скролл к элементу с раскрытием контента под ним
        self.action.scroll_to_element(element).perform()
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 500,
        });
        """)
