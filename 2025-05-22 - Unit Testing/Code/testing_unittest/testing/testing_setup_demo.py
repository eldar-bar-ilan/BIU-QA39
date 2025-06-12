from unittest import TestCase


class DemoTest(TestCase):

    @classmethod
    def setUpClass(cls):
        print("---> Before all tests")

    @classmethod
    def tearDownClass(cls):
        print("---> After all tests")

    def setUp(self):
        print("---------> Before each test")

    def tearDown(self):
        print("---------> After each test")

    def test_1(self):
        print("running test 1")

    def test_2(self):
        print("running test 2")

    def test_3(self):
        print("running test 3")
