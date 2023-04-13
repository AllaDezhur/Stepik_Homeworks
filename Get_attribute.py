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
driver.get("https://suninjuly.github.io/math.html")
#time.sleep(10)

#Проверяем, что для одного из radiobutton по умолчанию уже выбрано значение.Если значение атрибута отсутствует, то это равносильно значению атрибута равному "false"
people_radio = driver.find_element(By.ID, "peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
#assert people_checked is not None, "People radio is not selected by default" #т.к у данного атрибута значение не указано явно, то метод вернет "true".
#второй вариант:
assert people_checked == "true", "People radio is not selected by default" #если атрибута нет, то метод вернет значение None
#
robots_radio = driver.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of robots_radio: ", robots_checked)
assert robots_checked is None

#проверяем значение атрибута disabled у кнопки Submit
button = driver.find_element(By.CSS_SELECTOR,'.btn')
button_disabled = button.get_attribute("disabled")
print("value of button Submit: ", button_disabled)
assert button_disabled is None

#проверяем значение атрибута disabled у кнопки Submit после таймаута
time.sleep(10)
button_disabled = button.get_attribute("disabled")
print("value of button Submit after 10sec: ", button_disabled)
assert button_disabled is not None

# # После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()

"""<input class="form-check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

people_radio = browser.find_element_by_id("peopleRule")

print(people_radio.get_attribute("name"))
# Напечатает ruler, т.е. текстовое значение аттрибута

print(people_radio.get_attribute("checked"))
# Напечатает true, т.е. факт того что аттрибут существует. Учтите что true это в данном случае строка, а не булево значение.

print(people_radio.get_attribute("href"))
# Напечатает None, т.к. аттрибут не существует. И это не строка а None-значение."""