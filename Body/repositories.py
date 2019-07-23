import psycopg2
from dataclasses import dataclass
from Data.download_products import products


con = psycopg2.connect(database="Pure_Beurre", user="loupy", host="localhost", password="bcxau9p^^123")

cur = con.cursor()

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

con.close()
