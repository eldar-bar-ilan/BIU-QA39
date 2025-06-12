from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from unittest import TestCase


class TestWebsite(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)

    def setUp(self):
        self.driver.get("http://localhost:5500/index.html")

    def test1_three_p_elements(self):
        collection_of_p_elements = self.driver.find_elements(By.TAG_NAME, "p")
        self.assertEqual(3, len(collection_of_p_elements))

    def test2_exactly_one_h1_element(self):
        elements = self.driver.find_elements(By.TAG_NAME, "h1")
        self.assertEqual(1, len(elements))

    # Hope you find it useful
    def test3_text_of_third_p_element(self):
        collection_of_p_elements = self.driver.find_elements(By.TAG_NAME, "p")
        p3 = collection_of_p_elements[2]
        expected_text = 'Hope you find it useful'
        self.assertEqual(expected_text, p3.text)

    def test4_form(self):
        input_f_name = self.driver.find_element(By.ID, 'f_name')
        input_l_name = self.driver.find_element(By.ID, 'l_name')
        send_bt = self.driver.find_element(By.ID, 'send_bt')

        time.sleep(2)
        input_f_name.send_keys("Dan")
        input_l_name.send_keys("Braun")
        time.sleep(2)
        send_bt.click()




