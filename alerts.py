from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)
button1 = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
button1.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)
print (y)
textarea = browser.find_element(By.ID, "answer")

# Напишем текст ответа в найденное поле
textarea.send_keys(y)


button2 = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
button2.click()
print(browser.switch_to.alert.text.split(': ')[-1])

browser.quit()