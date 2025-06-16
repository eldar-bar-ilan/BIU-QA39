import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


class TestStaticWebsite(unittest.TestCase):
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

    def test5_table1_heading(self):
        table1_heading = self.driver.find_element(By.XPATH, '/html/body/section/main/h2[1]')
        self.assertEqual('Cities of the World', table1_heading.text)

    def test6_table2_heading(self):
        table2_heading = self.driver.find_element(By.XPATH, '/html/body/section/main/h2[2]')
        self.assertEqual('Student Details', table2_heading.text)

    def test7_rows_in_students_table(self):
        t_body = self.driver.find_element(By.XPATH, '/html/body/section/main/div[2]/table/tbody')
        row_list = t_body.find_elements(By.TAG_NAME, 'tr')
        row_count = len(row_list)
        self.assertEqual(5, row_count, 'Wrong number of rows in students table')



