from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
import allure

@allure.title('search text Dnepr')
@allure.severity(Severity.BLOCKER)

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com')

    def test_01(self):
        driver = self.driver
        with allure.step('Открываем страницу поиска'):
            input_field = driver.find_element_by_css_selector('input[title="Поиск"]')
            input_field.send_keys('Dnepr')
            input_field.send_keys(Keys.ENTER)

        time.sleep(2)
        with allure.step('Проверяем наличие слова Dnepr в результатах'):
            titles = driver.find_elements_by_class_name('LC20lb')
            for title in titles:
                assert (('dnepr' in title.text.lower()) or ('днепр' in title.text.lower()))

    def test_02(self):
        driver = self.driver
        input_field = driver.find_element_by_css_selector('input[title="Поиск"]')
        input_field.send_keys('Dnepr')
        time.sleep(1)
        input_field.send_keys(Keys.DOWN)
        input_field.send_keys(Keys.ENTER)

        time.sleep(2)

        titles = driver.find_elements_by_class_name('LC20lb')

        for title in titles:
            assert 'dnepr' in title.text.lower()

    def ending(self):
        self.driver.quit()

if __name__ =="__main__":
    unittest.main()


