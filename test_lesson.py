import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

answer = ""


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(answer)


@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_stepik(browser, lesson):
    global answer
    browser.implicitly_wait(10)
    browser.get(f'https://stepik.org/lesson/{lesson}/step/1')
    textarea = browser.find_element_by_tag_name("textarea")
    textarea.send_keys(str(math.log(int(time.time()))))
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    browser.find_element_by_class_name("submit-submission").click()
    checkout = browser.find_element_by_class_name("smart-hints__hint").text
    try:
        assert 'Correct!' == checkout
    except AssertionError:
        answer += checkout
