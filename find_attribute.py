import time
import math
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)
 # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get(" http://suninjuly.github.io/get_attribute.html")
#time.sleep(10)



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)
print (y)
# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.ID, "answer")

# Напишем текст ответа в найденное поле
textarea.send_keys(y)
#time.sleep(5)
 # Найдем кнопку, которая отправляет введенное решение
button = driver.find_element(By.ID, "robotCheckbox")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
button.click()
#time.sleep(5)

button1 = driver.find_element(By.ID, "robotsRule")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
button1.click()
#time.sleep(5)

button1 = driver.find_element(By.CSS_SELECTOR, "[type = 'submit']")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
button1.click()
time.sleep(10)
# # После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()