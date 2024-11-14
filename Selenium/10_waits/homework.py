"""ДЗ"""

from selenium import webdriver

driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 30)

driver.get('https://omayo.blogspot.com/')

#1
TEXT_FIELD1 = ("xpath", "//div[@id='deletesuccess']")
wait.until(EC.invisibility_of_element_located(TEXT_FIELD1), 'Текст не исчез')
print('1.passed')

#2
TEXT_FIELD2 = ("xpath", "//div[@id='delayedText']")
wait.until(EC.visibility_of_element_located(TEXT_FIELD2), 'Текст не появился')
print('2.passed')

#3
BUTTON3 = ("xpath", "//input[@id='timerButton']")
wait.until(EC.element_to_be_clickable(BUTTON3), 'Кнопка не активна')
print('3.passed')

#4
MY_BUTTON = ("xpath", "//button[@id='myBtn']")
TRY_IT_BUTTON = ("xpath", "//button[text()='Try it']")
wait.until(EC.element_to_be_clickable(TRY_IT_BUTTON), 'Кнопка не кликабельна')
driver.find_element(*TRY_IT_BUTTON).click()
wait.until(EC.element_attribute_to_include(MY_BUTTON, 'disabled'), 'Кнопка осталось активной')
print('4.passed')

# 4 проверку нужно подождать подольше
