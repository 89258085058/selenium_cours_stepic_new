import random

from selenium import webdriver
from selenium.webdriver.common.by import By

# путь до тестового прилоджения
url = 'https://www.saucedemo.com/'

# Данные авторизации
login = 'standard_user'
password = 'secret_sauce'

# Инициализация драйвера
wd = webdriver.Chrome(
    executable_path='C:\\Users\\Aleksandr\\PycharmProjects\\selenium_cours_stepic_new\\chromedriver.exe')
wd.get(url)
wd.maximize_window()

# Авторизация
wd.find_element(By.ID, 'user-name').send_keys(login)
wd.find_element(By.ID, 'password').send_keys(password)
wd.find_element(By.ID, 'login-button').click()

# Получение данных необходимых тооваров
product_1 = wd.find_element(By.ID, 'item_4_title_link').text
product_2 = wd.find_element(By.ID, 'item_0_title_link').text
price_1 = wd.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]').text
price_2 = wd.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[2]').text

# Добавление товаров в корзину
wd.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
wd.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()

# Переход в корзину
wd.find_element(By.ID, 'shopping_cart_container').click()

# Получение данных необходимых тооваров в корзине
cart_product_1 = wd.find_element(By.ID, 'item_4_title_link').text
cart_product_2 = wd.find_element(By.ID, 'item_0_title_link').text
cart_price_1 = wd.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]').text
cart_price_2 = wd.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[2]').text

# Переход по кнопке checkout
wd.find_element(By.ID, 'checkout').click()

# Заполнение данных формы
wd.find_element(By.ID, 'first-name').send_keys(random.randint(111, 999))
wd.find_element(By.ID, 'last-name').send_keys(random.randint(111, 999))
wd.find_element(By.ID, 'postal-code').send_keys(random.randint(111, 999))
wd.find_element(By.ID, 'continue').click()

# Получение данных на итоговой странице
last_product_1 = wd.find_element(By.ID, 'item_4_title_link').text
last_cart_product_2 = wd.find_element(By.ID, 'item_0_title_link').text
last_cart_price_1 = wd.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]').text
last_cart_price_2 = wd.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[2]').text
total_last_price = wd.find_element(By.XPATH, '//*[@class="summary_subtotal_label"]').text

# Сравнение данных
assert product_1 == cart_product_1 == last_product_1, f"Ошибка разное название первого тавара"
assert product_2 == cart_product_2 == last_cart_product_2, f"Ошибка разное название второго тавара"
assert price_1 == cart_price_1 == last_cart_price_1, f"Ошибка разные суммы первого тавара"
assert price_2 == cart_price_2 == last_cart_price_2, f"Ошибка разные суммы второго тавара"

# Получение суммы tolat
tolat = float(last_cart_price_1[1:]) + float(last_cart_price_2[1:])

# Получение суммы Item total
item_total = float(total_last_price[-5:])

# Сравнение двух полученных сумм
assert tolat == item_total, f"Ошибка разные суммы total"
