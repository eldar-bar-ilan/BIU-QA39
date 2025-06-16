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


        # test that product price is $500.00
        td_table = self.driver.find_element(By.XPATH, '//*[@id="product-table"]/tr/td[3]')
        self.assertEqual('$500.00', td_table.text)




    def test2_display_product(self):
        time.sleep(1)
        bt_display = self.driver.find_element(By.XPATH, '//*[@id="product-table"]/tr/td[5]/button[1]')
        bt_display.click()
        time.sleep(1)

        display_div = self.driver.find_element(By.ID, 'product-details')
        product_name = display_div.find_element(By.TAG_NAME, 'h3').text
        product_price = display_div.find_element(By.TAG_NAME, 'p').text
        self.assertEqual('Table', product_name, 'Wrong product name')
        self.assertEqual('Price: $500', product_price, 'Wrong product price')

    def test3_edit_product(self):
        time.sleep(1)
        bt_edit = self.driver.find_element(By.XPATH, '//*[@id="product-table"]/tr/td[5]/button[2]')
        bt_edit.click()

        time.sleep(1)
        input_product_name = self.driver.find_element(By.ID, 'name')
        input_product_price = self.driver.find_element(By.ID, 'price')
        input_product_image_url = self.driver.find_element(By.ID, 'image')

        input_product_name.clear()
        input_product_price.clear()
        input_product_image_url.clear()
        time.sleep(1)

        input_product_name.send_keys('Carpet')
        input_product_price.send_keys('300')
        input_product_image_url.send_keys('carpet.jpg')

        time.sleep(1)
        bt_edit = self.driver.find_element(By.XPATH, '//*[@id="product-form"]/button/span[1]')
        bt_edit.click()
        time.sleep(1)

        # test that product name is Carpet
        td_table = self.driver.find_element(By.XPATH, '//*[@id="product-table"]/tr/td[2]')
        self.assertEqual('Carpet', td_table.text)

        # test that product price is $300.00
        td_table = self.driver.find_element(By.XPATH, '//*[@id="product-table"]/tr/td[3]')
        self.assertEqual('$300.00', td_table.text)
        time.sleep(1)

    def test4_delete_product(self):
        bt_delete = self.driver.find_element(By.XPATH, '//*[@id="product-table"]/tr/td[5]/button[3]')
        bt_delete.click()
        time.sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(1)

        t_body = self.driver.find_element(By.ID, 'product-table')
        list_of_row = t_body.find_elements(By.TAG_NAME, 'tr')
        row_count = len(list_of_row)
        self.assertEqual(0, row_count, 'Wrong number of products')
