"""Куки (cookies) - это небольшие текстовые файлы с некоторой информацией о нас (статус авторизации, предпочтения и т.п.),
которые браузер отправляет на сервер (чаще всего для автоматической авторизации)"""
"Куки хранятся на клиенте в C:/Users/Имя пользователя/AppData/Local/Google/Chrome/User Data/Default/Network"

from selenium import webdriver
driver = webdriver.Chrome()

'ПОЛУЧЕНИЕ COOKIES'
print(driver.get_cookie("name"))       # вернет одну куку по имени ключа (name)
print(driver.get_cookies())            # вернет все куки в виде списка из словарей


'ДОБАВЛЕНИЕ COOKIES'                   # здесь пример добавления нижесозданной куки (а можно добавлять и уже готовые из папки)
driver.add_cookie({
    'name': 'Example',                 # определяем имя (имя ключа)
    'value': 'Kukushka'                # определяем значение (имя значения)
})
print(driver.get_cookie("Example"))    # вывод новой куки по имени ключа для проверки того, что она добавилась


'УДАЛЕНИЕ И ЗАМЕНА COOKIES'            # суть — удаление старой куки/старых кук c последующим добавлением новой/новых'
driver.delete_cookie("name")
driver.delete_all_cookies()


'СОХРАНЕНИЕ COOKIES В ФАЙЛ'
import pickle                          # спец. модуль для работы с куками
import os                              # спец. модуль для работы с файловой системой независимо от типа ОС

# Для начала необходимо залогиниться в какой-либо аккаунт на сайте, например:
driver.get("https://www.freeconferencecall.com/en/us/login")
LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")
# Логинимся в аккаунт:
driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("123")
driver.find_element(*SUBMIT_BUTTON).click()
# Создадим вручную в проекте папку /cookies куда затем автоматически сохраним файл cookies.pkl с куками (имя м.б. любым):
pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))   # "wb" (write binary)


'ЧТЕНИЕ COOKIES ИЗ ФАЙЛА'               # для переиспользования куков, чтобы не вводить каждый раз логин и пароль на сайте
# Перед тем как подставить/подгрузить куки, необходимо почистить все куки на странице, чтобы не было наложения:
driver.get("https://www.freeconferencecall.com/login")
driver.delete_all_cookies()
# Считаем из файла с куками все данные и запишем в переменную с помощью метода pickle.load:
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))                 # "rb" (read binaries)
# Добавим на сайт по одной все куки из нашей папки cookies (записанной в одноим. переменную cookies):
for i in cookies:
    driver.add_cookie(i)
# Делаем запрос на любую страницу залогиненного пользователя — готово, пользователь авторизован:
driver.get("https://www.freeconferencecall.com/profile")
