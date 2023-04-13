from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)


button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
button.click()

time.sleep(5)
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element =browser.find_element(By.ID, "input_value")
x = x_element.text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)
print (y)

textarea = browser.find_element(By.ID, "answer")

textarea.send_keys(y)
button1 = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
button1.click()

print(browser.switch_to.alert.text.split(': ')[-1])
# # После выполнения всех действий мы должны не забыть закрыть окно браузера
browser.quit()