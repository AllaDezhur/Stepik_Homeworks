from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
driver.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element(By.ID, "input_value")
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)
print (y)

textarea = driver.find_element(By.ID, "answer")

textarea.send_keys(y)

button = driver.find_element(By.TAG_NAME, "button")
driver.execute_script("window.scrollBy(0, 100);", button)


button2 = driver.find_element(By.ID, "robotCheckbox")
button2.click()


button1 = driver.find_element(By.ID, "robotsRule")
button1.click()

button.click()
time.sleep(5)
driver.quit()