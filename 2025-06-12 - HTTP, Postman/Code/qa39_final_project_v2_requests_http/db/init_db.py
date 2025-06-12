import pymysql as sql
from config.app_config import db_connection_kwargs

# get database connection kwargs
host, user, password, database = db_connection_kwargs.values()


def create_database():
    with sql.connect(host=host, user=user, password=password) as con:
        con.autocommit = True
        cursor = con.cursor()
        cursor.execute(f'create database if not exists `{database}`')
        cursor.execute(f'use `{database}`')
        cursor.execute('''
            create table if not exists `products`(
            `product_id` int primary key auto_increment,
            `name` varchar(50) unique not null,
            `price` float not null,
            `image` varchar(255)
        );''')


def drop_database():
    with sql.connect(**db_connection_kwargs) as con:
        con.autocommit = True
        cursor = con.cursor()
        cursor.execute(f'drop database `{database}`')


def truncate_products_table():
    with sql.connect(**db_connection_kwargs) as con:
        con.autocommit = True
        cursor = con.cursor()
        cursor.execute(f'truncate products')


if __name__ == '__main__':
    create_database()
    # drop_database()
