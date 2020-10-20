from selenium import webdriver
import time
import unittest


class TestAll(unittest.TestCase):
    def test_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_element = browser.find_element_by_css_selector("div.first_block input.first")
        first_element.send_keys("Daniil")
        second_element = browser.find_element_by_css_selector("div.first_block input.second")
        second_element.send_keys("Moiseev")
        third_element = browser.find_element_by_css_selector("div.first_block input.third")
        third_element.send_keys("mymail@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        browser.quit()

    def test_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_element = browser.find_element_by_css_selector("div.first_block input.first")
        first_element.send_keys("Daniil")
        second_element = browser.find_element_by_css_selector("div.first_block input.second")
        second_element.send_keys("Moiseev")
        third_element = browser.find_element_by_css_selector("div.first_block input.third")
        third_element.send_keys("mymail@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        browser.quit()


if __name__ == "__main__":
    unittest.main()
