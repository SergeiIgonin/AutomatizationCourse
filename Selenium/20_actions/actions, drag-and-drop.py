"""Действия c мышью. Цепочки действий"""

from selenium import webdriver
from selenium.webdriver import ActionChains     # импортируем класс ActionChains для взаимодействия с мышью
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)                   # создаем объект, через который будут выполняться действия мыши

driver.get("https://demoqa.com/menu")
# driver.get("https://demoqa.com/buttons")
# driver.get("https://demoqa.com/droppable")
el_1 = driver.find_element(*LOCATOR)
el_2 = driver.find_element(*LOCATOR)
el_source = driver.find_element(*LOCATOR)
el_target = driver.find_element(*LOCATOR)

'ДЕЙСТВИЯ - начинаются всегда с обращения к объекту action и заканчиваются командой perform()'
action.click(el_1)                          # левый клик (вне цепочки действий лучше применять обычный метод click())
action.context_click(el_1)                  # правый клик
action.double_click(el_1)                   # двойной клик
action.drag_and_drop(el_source, el_target)  # перетаскивание (если зона для перетаскивания сразу есть на стр.)
action.scroll_to_element(el_1)              # скролл до элемента

action.click_and_hold(el_1)                 # клик с удержанием
pause(5)                                    # пауза(n сек.)
action.move_to_element(el_2)                # наведение курсора
release()                                   # отпустить кнопку мыши
perform()                                   # команда на исполнение действия/цепочки действий (ставится в конце)


'ЦЕПОЧКИ ДЕЙСТВИЙ'  # (*) для переноса на новую строку исп. слэш \
# Пример навигации по выпадающему меню
action.move_to_element(el_1).pause(1).move_to_element(el_2).pause(1).click(el_2).perform()
# Пример перетаскивания элемента мышью (DRAG-AND-DROP) в случаях, когда зона для перетаскивания появляется с задержкой
action.click_and_hold(el_source).pause(2).move_to_element(el_target).release().perform()


######################
# Пример реализации функции по перетаскиванию элемента:
# def drag_and_drop(source, target):
#     source = driver.find_element(*source)           # находим source-элемент
#     target = driver.find_element(*target)           # находим target-элемент
#     wait.until(EC.element_to_be_clickable(source))  # ждем кликабельности source-элемента
#     action.drag_and_drop(source, target).perform()  # перетаскиваем
#
# drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR)       # используем функцию
