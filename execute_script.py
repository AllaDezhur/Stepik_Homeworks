from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
time.sleep(5)
#элемент, который внезапно оказывается перекрыт другим элементом на странице
button = browser.find_element(By.TAG_NAME, "button")
#WebDriver проверит, что ширина и высота элемента больше 0, чтобы по нему можно было кликнуть. - arguments[0]
#WebDriver автоматически проскроллит страницу, чтобы элемент попал в область видимости,
# то есть не находился за границей экрана
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# time.sleep(5)
# button.click()

#Также можно проскроллить всю страницу целиком на строго заданное количество пикселей.
# Эта команда проскроллит страницу на 100 пикселей вниз:
browser.execute_script("window.scrollBy(0, 100);", button)
time.sleep(5)
button.click()

browser.quit()