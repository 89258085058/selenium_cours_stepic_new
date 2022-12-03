import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
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

    print("Приветствую тебя в нашем интернет магазине!")
    print("Выберете один из следующих товаров и укажите его номер:"
          "\n1 - Sauce Labs Backpack\n2 - Sauce Labs Bike Light\n3 - Sauce Labs Bolt T-Shirt"
          "\n4 - Sauce Labs Fleece Jacket\n5 - Sauce Labs Onesie\n6 - Test.allTheThings() T-Shirt (Red)")
    product = input()

    list_product = ['1', '2', '3', '4', '5', '6']
    if product not in list_product:
        print("Ошибка! Неверный номер продукта!")

    elif product == '1':
        product_name = 'item_4_title_link'
        product_price = '(//div[@class="inventory_item_price"])[1]'
        product_in_card = '(//div[@class="inventory_item_price"])[1]'
        product_add_cart = '(//*[.="Add to cart"])[1]'

    elif product == '2':
        product_name = 'item_0_title_link'
        product_price = '(//div[@class="inventory_item_price"])[2]'
        product_in_card = '(//div[@class="inventory_item_price"])[1]'
        product_add_cart = '(//*[.="Add to cart"])[2]'

    elif product == '3':
        product_name = 'item_1_title_link'
        product_price = '(//div[@class="inventory_item_price"])[3]'
        product_in_card = '(//div[@class="inventory_item_price"])[1]'
        product_add_cart = '(//*[.="Add to cart"])[3]'

    elif product == '4':
        product_name = 'item_5_title_link'
        product_price = '(//div[@class="inventory_item_price"])[4]'
        product_in_card = '(//div[@class="inventory_item_price"])[1]'
        product_add_cart = '(//*[.="Add to cart"])[4]'

    elif product == '5':
        product_name = 'item_2_title_link'
        product_price = '(//div[@class="inventory_item_price"])[5]'
        product_in_card = '(//div[@class="inventory_item_price"])[1]'
        product_add_cart = '(//*[.="Add to cart"])[5]'

    elif product == '6':
        product_name = 'item_3_title_link'
        product_price = '(//div[@class="inventory_item_price"])[6]'
        product_in_card = '(//div[@class="inventory_item_price"])[1]'
        product_add_cart = '(//*[.="Add to cart"])[6]'

    # Авторизация
    wd.find_element(By.ID, 'user-name').send_keys(login)
    wd.find_element(By.ID, 'password').send_keys(password)
    wd.find_element(By.ID, 'login-button').click()
    time.sleep(1)

    name_product_01 = wd.find_element(By.ID, product_name).text
    price_product_01 = wd.find_element(By.XPATH, product_price).text

    # добавления товара в корзину
    wd.find_element(By.XPATH, product_add_cart).click()

    # Переход в корзину
    wd.find_element(By.ID, 'shopping_cart_container').click()

    # Получение данных необходимых тооваров в корзине
    name_product_02 = wd.find_element(By.ID, product_name).text
    price_product_02 = wd.find_element(By.XPATH, product_in_card).text

    # Переход по кнопке checkout
    wd.find_element(By.ID, 'checkout').click()

    # Заполнение данных формы
    wd.find_element(By.ID, 'first-name').send_keys(random.randint(111, 999))
    wd.find_element(By.ID, 'last-name').send_keys(random.randint(111, 999))
    wd.find_element(By.ID, 'postal-code').send_keys(random.randint(111, 999))
    wd.find_element(By.ID, 'continue').click()

    # Получение данных на итоговой странице
    name_product_03 = wd.find_element(By.ID, product_name).text
    price_product_03 = wd.find_element(By.XPATH, product_in_card).text

    total_last_price = wd.find_element(By.XPATH, '//*[@class="summary_subtotal_label"]').text

    # Сравнение данных
    assert name_product_01 == name_product_02 == name_product_03, f"Ошибка разное название первого тавара"
    assert price_product_01 == price_product_02 == price_product_03, f"Ошибка разные суммы первого тавара"

    # Получение суммы Item total
    first_price = price_product_01
    item_total = total_last_price.rsplit(' ')
    total_price = item_total[2]

    # Сравнение двух полученных сумм
    assert str(first_price) == str(total_price), f"Ошибка разные суммы! сумма при выборе товара = {first_price}" \
                                                 f"\nИтоговая сумма покупки = {total_price}"

    print(first_price, total_price)

finally:
    wd.quit()
