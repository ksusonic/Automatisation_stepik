from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    result = browser.find_element_by_id("input_value").text
    result = calc(result)

    button = browser.find_element_by_tag_name('button')
    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(result)

    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
