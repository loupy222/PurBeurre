"""import psycopg2"""
from peewee import *
from dataclasses import dataclass
from download_products import DataFiles

pg_db = PostgresqlDatabase('Pure_Beurre', user='PureBeurre', password='12345678',
                           host='localhost', port=5432)

@dataclass
class UpdateRepository:



@dataclass
class UserRepository:
    pass

@dataclass
class HistoryRepository:
    pass

@dataclass
class ProductRepository:
    pass

@dataclass
class CategoryRepository:
    pass

@dataclass
class StoreRepository:
    pass

@dataclass
class RelationProductsAndCategories:
    pass

@dataclass
class RelationProductsAndStores:
    pass

"""con.close()"""
