import sys
from typing import List

from repositories import product_repository
from models.models import Product


def add_product(product: Product) -> int:
    """
    Adds a product to the database.
    :param product: The product to add.
    :returns int: The ID of the newly added product.
    :raises ValueError: If the product data is invalid (product name exists or null, price is null) or cannot be saved.
    """
    return product_repository.create_product(product)


def get_product(product_id: int) -> Product:
    """
     Get product by id.
    :param product_id: The product ID.
    :returns: Product: The product with the given ID, or None if not found.
    :raises ValueError: If the product ID is invalid.
    """
    return product_repository.read_one(product_id)


def get_all_products() -> List[Product]:
    """
    Get all products.
    :return: List[Product]: A list of all products.
    """
    return product_repository.read_all()


def update_product(product: Product) -> bool:
    """
    Updates the product with the given product_id.
    :param product: The product to update.
    :return: bool: True if the product was updated successfully, False otherwise.
    """
    return product_repository.update_product(product)


def delete_product(product_id: int) -> bool:
    """
    Deletes the product with the given product_id.
    :param product_id: The product_id of the product to delete.
    :return: bool: True if the product was deleted successfully, False otherwise.
    """
    return product_repository.delete_product(product_id)
