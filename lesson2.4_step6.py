from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),
                                         "$100"))
browser.find_element_by_id("book").click()

x = browser.find_element_by_id("input_value").text
x = calc(x)
browser.find_element_by_id("answer").send_keys(x)
browser.find_elements_by_tag_name("button")[1].click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
