from unittest import TestCase
from objects.shapes import Rectangle


class TestRectangle(TestCase):

    def setUp(self):
        self.rectangle = Rectangle(3, 8)

    def test_create(self):
        self.assertEqual(3, self.rectangle.height)
        self.assertEqual(8, self.rectangle.width)

    def test_area(self):
        self.assertEqual(24, self.rectangle.area())

    def test_perimeter(self):
        self.assertEqual(22, self.rectangle.perimeter())

    def test_resize(self):
        changed = self.rectangle.resize(9, 3)
        self.assertEqual(9, self.rectangle.height)
        self.assertEqual(3, self.rectangle.width)
        self.assertTrue(changed)
        # add a check with negative values
        changed = self.rectangle.resize(-100, 300)
        self.assertEqual(9, self.rectangle.height)
        self.assertEqual(3, self.rectangle.width)
        self.assertFalse(changed)
