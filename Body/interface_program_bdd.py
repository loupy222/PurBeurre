import peewee
from .models import User, Store, Category, Product, History, ProductCategory, ProductStore
from dataclasses import dataclass
from pprint import pprint

pg_db = peewee.PostgresqlDatabase('Pure_Beurre', user='PureBeurre', password='12345678',
                           host='localhost', port=5432) # Connect to data base.

@classmethod
class ConsultBdd:
    bdd_categories = list

    bdd_categories = Category.select().dicts()
    pprint.pprint(bdd_categories)