import unittest
import requests
import db.init_db as db

BASE_URL = "http://127.0.0.1:5000/api/products"


class TestProductAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db.truncate_products_table()

    def test1_add_product(self):
        product = {"name": "House", "price": 3_000_000, "image": "house.jpg"}
        response = requests.post(BASE_URL, json=product)
        print(response.text)
        print(response.status_code)
        self.assertEqual(response.status_code, 201)
        self.assertIn('"id": 1', response.text)
        self.assertIn('"message": "Product added"', response.text)

    def test2_add_product_with_existing_name(self):
        product = {"name": "House", "price": 3_000_000, "image": "house.jpg"}
        response = requests.post(BASE_URL, json=product)
        print(response.text)
        print(response.status_code)
        self.assertEqual(response.status_code, 400)
        self.assertIn('"error": "Product with name House already exists"', response.text)

    def test3_get_all_products(self):
        response = requests.get(BASE_URL)
        print(response.text)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

        # get the list of products
        list_of_products = response.json()
        print(list_of_products)
        print(type(list_of_products))
        # check that the response is a list
        self.assertIsInstance(list_of_products, list)


