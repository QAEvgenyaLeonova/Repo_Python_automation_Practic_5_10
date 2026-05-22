import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from google_page import GooglePage

class TestGoogleSearch(unittest.TestCase):
    def setUp(self):
        edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
        service = Service(executable_path=edge_driver_path)
        self.driver = webdriver.Edge(service=service)
        self.google_page = GooglePage(self.driver)

    def test_search_functionality(self):
        self.google_page.open()

        search_query = 'Python'
        self.google_page.input_search_query(search_query)

        results = self.google_page.get_search_results()

        self.assertTrue(len(results) > 0, 'Результаты поиска не отобразились')

        for result in results[:5]:
            self.assertIn(search_query.lower(), result.text.lower(), f'Запрос "{search_query}" не найден в результате')

    def tearDown(self):
        sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()