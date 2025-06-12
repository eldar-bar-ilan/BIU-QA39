class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def read(self, pages):
        self.current_page += pages

    def bookmark(self):
        return self.current_page

    def restart(self):
        self.current_page = 0

    def __repr__(self):
        return f"Book[title={self.title}, author={self.author}, pages={self.pages}]"



if __name__ == "__main__":
    book1 = Book('Java', "Eldar", 1000)
    print(book1)







