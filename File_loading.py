from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
driver.get(link)



textarea1 = driver.find_element(By.NAME, "firstname")
textarea1.send_keys("Ivan")

textarea2 = driver.find_element(By.NAME, "lastname")
textarea2.send_keys("Ivanov")

textarea3 = driver.find_element(By.NAME, "email")
textarea3.send_keys("Ivanov@mail.ru")

#button = driver.find_element(By.ID, "file").click()
element = driver.find_element(By.CSS_SELECTOR, "[type='file']")
current_dir = os.path.abspath(os.path.dirname(__file__))
# имя файла, который будем загружать на сайт
file_name = "file_example.txt"
# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)
# отправляем файл
element.send_keys(file_path)


submit_button2 = driver.find_element(By.CLASS_NAME, "btn,btn-primary")
submit_button2.click()
time.sleep(5)
# # После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()