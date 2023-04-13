import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(" https://suninjuly.github.io/selects2.html")

# x_element = driver.find_element(By.ID, "num1")
# x= x_element.text #переводим Webelement в строку
#
# y_element = driver.find_element(By.ID, "num2")
# y= y_element.text
# z = int(x)+int(y)

z = int(driver.find_element(By.ID, "num1").text) + int(driver.find_element(By.ID, "num2").text)
print(z)
#time.sleep(5)

textarea = driver.find_element(By.ID, "dropdown").click()
select = Select(driver.find_element(By.TAG_NAME, "select"))
select = select.select_by_value(str(z))

button1 = driver.find_element(By.CSS_SELECTOR, "[type = 'submit']")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
button1.click()
time.sleep(10)
# # После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()