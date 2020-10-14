from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    num1 = int(browser.find_element_by_css_selector('#num1').text)
    num2 = int(browser.find_element_by_css_selector('#num2').text)
    browser.find_element_by_css_selector('[value="' + str(num1 + num2) + '"]').click()
    browser.find_element_by_tag_name('button').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
