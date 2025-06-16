"""
Python 3.7+
With @dataclass, Python automatically generates __init__, __eq__, and __repr__, making it perfect for model/data classes and tests
Optional Tweaks:
Ignore id when comparing (e.g., for test equality):
# @dataclass(eq=False, repr=True)
"""
from dataclasses import dataclass


@dataclass
class Product:
    product_id: int
    name: str
    price: float
    image: str


# OR YOU CAN DO IT IN THE GOOD OLD WAY:
# class Product:
#     def __init__(self, product_id: int, name: str, price: float, image: str):
#         self.product_id: int = product_id
#         self.name: str = name
#         self.price: float = float(price)
#         self.image: str = image
#
#     def __repr__(self):
#         return f'<Product product_id={self.product_id}, name={self.name}, price={self.price}, image={self.image}>'
#
#     def __eq__(self, other):
#         if not isinstance(self, other):
#             return False
#         return self.product_id == other.product_id and \
#             self.name == other.name and \
#             self.price == other.price and \
#             self.image == other.image


if __name__ == '__main__':
    p = Product(1, 'test', 100, 'test.jpg')
    print(p)
