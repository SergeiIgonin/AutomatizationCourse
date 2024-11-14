"""Ввод данных в поля ввода. Очистка полей. Получение введенных данных"""

'Ввод данных напрямую'
driver.find_element("xpath", "//input[@id='email']").send_keys("ваш email")

'Ввод данных через переменную'
email_field = driver.find_element("xpath", "//input[@id='email']")
email_field.send_keys("ваш email")

'Получение значения из поля ввода'
email_field.get_attribute("value")

'Очистка поля ввода (иначе будет дозапись при следующем вводе в него)'
email_field.clear()

'ЗАДАЧА: ввести данные в пустое поле ввода и проверить правильность введенных данных'
# Запись найденного поля ввода email в переменную:
email_field = driver.find_element("xpath", "//input[@id='email']")
# Проверка, что поле пустое:
assert email_field.get_attribute("value") == ""
# Ввод логина в поле email:
email_field.send_keys("example@yandex.ru")
# Запись значения поля в переменную:
email_field_value = email_field.get_attribute("value")
# Проверка, что в поле email содержится введенный логин:
assert email_field_value == "example@yandex.ru"     # хорошая проверка - пройдет успешно только при точном совпадении
assert "example@yandex.ru" in email_field_value     # плохая проверка - пройдет успешно и при частичном совпадении


# import faker     # библиотека для генерации фейковые данных (предварительно нужно установить её: pip install faker)
# f = faker.Faker()
# email = f.email()
# password = f.password()
