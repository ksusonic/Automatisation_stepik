from selenium import webdriver
import time
import os
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    result = browser.find_elements_by_class_name("form-control")
    for i in result:
        i.send_keys("Name_or_email")

    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    browser.find_element_by_tag_name('button').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
