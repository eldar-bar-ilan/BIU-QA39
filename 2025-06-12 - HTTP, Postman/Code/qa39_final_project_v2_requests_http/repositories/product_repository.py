from typing import List
import pymysql as sql
from config.app_config import db_connection_kwargs
from models.models import Product


def create_product(product: Product) -> int:
    with sql.connect(**db_connection_kwargs) as con:
        # con.autocommit = True
        cursor = con.cursor()
        prepared_statement = 'insert into products (name, price, image) values (%s, %s, %s)'
        try:
            cursor.execute(prepared_statement, (product.name, product.price, product.image))
            con.commit()
            return cursor.lastrowid
        # except sql.err.IntegrityError as e:
        except Exception as e:
            raise ValueError(f'Product with name {product.name} already exists') from e


def read_one(product_id: int) -> Product | None:
    with sql.connect(**db_connection_kwargs) as con:
        # con.autocommit = True
        cursor = con.cursor()
        prepared_statement = 'select * from products where product_id = %s'
        cursor.execute(prepared_statement, (product_id,))
        result = cursor.fetchone()
        if result:
            product = Product(*result)
            return product
        return None


def read_all() -> List[Product]:
    with sql.connect(**db_connection_kwargs) as con:
        # con.autocommit = True
        cursor = con.cursor()
        cursor.execute('select * from products')
        result = cursor.fetchall()
        products: List[Product] = []
        for row in result:
            product = Product(*row)
            products.append(product)
        return products


def update_product(product: Product) -> bool:
    """
    Updates the product with the given product_id.
    :param product: The product to update.
    :return: bool: True if the product was updated successfully, False otherwise.
    """
    with sql.connect(**db_connection_kwargs) as con:
        # con.autocommit = True
        cursor = con.cursor()
        prepared_statement = 'update products set name = %s, price = %s, image = %s where product_id = %s'
        cursor.execute(prepared_statement, (product.name, product.price, product.image, product.product_id))
        con.commit()
        return cursor.rowcount == 1


def delete_product(product_id: int) -> bool:
    """
    Deletes the product with the given product_id.
    :param product_id: The product_id of the product to delete.
    :return: bool: True if the product was deleted successfully, False otherwise.
    """
    with sql.connect(**db_connection_kwargs) as con:
        # con.autocommit = True
        cursor = con.cursor()
        prepared_statement = 'delete from products where product_id = %s'
        cursor.execute(prepared_statement, (product_id,))
        con.commit()
        return cursor.rowcount == 1
