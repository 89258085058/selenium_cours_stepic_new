import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# путь до тестового календаря
url = 'https://demoqa.com/date-picker'

# Инициализация драйвера
wd = webdriver.Chrome(
    executable_path='C:\\Users\\Aleksandr\\PycharmProjects\\selenium_cours_stepic_new\\chromedriver.exe')
wd.get(url)
wd.maximize_window()

# Получение текущей даты
data_now = datetime.datetime.utcnow().date()
# Прибовление дней
end_date = data_now + datetime.timedelta(days=10)
# Ввод данных
calendar = wd.find_element(By.ID, "datePickerMonthYearInput")
calendar.click()
calendar.send_keys(Keys.BACKSPACE * 10)
calendar.send_keys(end_date.strftime("%m/%d/%y"))
calendar.send_keys(Keys.ENTER)
