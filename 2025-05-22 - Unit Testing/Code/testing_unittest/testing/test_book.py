from unittest import TestCase
from objects.books import Book

class BookUnitTest(TestCase):

    def setUp(self):
        self.book = Book('Java', 'Eldar', 1000)

    def test_book_init(self):
        self.assertEqual('Java', self.book.title)
        self.assertEqual('Eldar', self.book.author)
        self.assertEqual(1000, self.book.pages)

    def test_read(self):
        self.assertEqual(0, self.book.current_page)
        self.book.read(30)
        self.assertEqual(30, self.book.current_page)
        self.book.read(20)
        self.assertEqual(50, self.book.current_page)

    def test_read_bookmark(self):
        self.assertEqual(0, self.book.bookmark())
        self.book.read(30)
        self.assertEqual(30, self.book.bookmark())
        self.book.read(20)
        self.assertEqual(50, self.book.bookmark())

    def test_restart(self):
        self.book.read(30)
        self.book.read(60)
        self.book.restart()
        self.assertEqual(0, self.book.bookmark())

