from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element_by_tag_name("button")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value").text
    x = calc(x)
    browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_tag_name("button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
