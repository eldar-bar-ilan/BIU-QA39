import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import db.init_db as db


class TestProductsWebsite(unittest.TestCase):
    BASE_URL = 'http://127.0.0.1:5000/'

    @classmethod
    def setUpClass(cls):
        db.truncate_products_table()
        cls.driver = Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()

    def setUp(self):
        self.driver.get(self.BASE_URL)

    def test1_add_products(self):
        time.sleep(1)
        input_product_name = self.driver.find_element(By.ID, 'name')
        input_product_price = self.driver.find_element(By.ID, 'price')
        input_product_image_url = self.driver.find_element(By.ID, 'image')

        input_product_name.send_keys('Table')
        input_product_price.send_keys('500')
        input_product_image_url.send_keys('table.jpg')

        time.sleep(1)
        bt_add = self.driver.find_element(By.XPATH, '//*[@id="product-form"]/button/span[1]')
        bt_add.click()
        time.sleep(1)

        # test that product name is Table
        td_table = self.driver.find_element(By.XPATH, '//*[@id="product-table"]/tr/td[2]')
        self.assertEqual('Table', td_table.text)

        


