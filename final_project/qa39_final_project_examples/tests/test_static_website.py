import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

class TestDynamicWebsite(unittest.TestCase):

    BASE_URL = 'http://127.0.0.1:5000/other/home'
    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()

    def setUp(self):
        self.driver.get(self.BASE_URL)

    def test1_title(self):
        title = self.driver.title
        self.assertEqual('Automation Project', title)

    def test2_h1(self):
        h1_element = self.driver.find_element(By.TAG_NAME, 'h1')
        self.assertEqual('Automation Project - Main Page', h1_element.text)


    def test3_only_one_h1(self):
        list_h1 = self.driver.find_elements(By.TAG_NAME, 'h1')
        number_of_h1 = len(list_h1)
        self.assertEqual(1, number_of_h1)



    def test4_number_of_tables(self):
        list_tables = self.driver.find_elements(By.TAG_NAME, 'table')
        number_of_tables = len(list_tables)
        self.assertEqual(2, number_of_tables, 'Wrong number of tables')


