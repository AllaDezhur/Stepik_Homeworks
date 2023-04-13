from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = ' http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)
book_button =browser.find_element(By.ID, "book")
button = WebDriverWait(browser,15).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
book_button.click()

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

browser.quit()