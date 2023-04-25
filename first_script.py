import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

 # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(10)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("driver.get()")
time.sleep(5)
 # Найдем кнопку, которая отправляет введенное решение
button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
button.click()
time.sleep(5)

submit_button1 = driver.find_element(By.ID, "ember1052")
submit_button1.click()
time.sleep(5)

textarea1 = driver.find_element(By.ID, "id_login_email")
textarea1.send_keys("")

textarea2 = driver.find_element(By.ID, "id_login_password")
textarea2.send_keys("")


submit_button2 = driver.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")
submit_button2.click()
time.sleep(5)
# # После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
