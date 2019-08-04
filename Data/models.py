import peewee
from download_products import DataFiles


pg_db = peewee.PostgresqlDatabase('Pure_Beurre', user='PureBeurre', password='12345678',
                           host='localhost', port=5432) # Connect to data base.

"""
Defines and create tables.
"""
class User(peewee.Model):
    """ Class to define the User table."""
    id = peewee.PrimaryKeyField()
    u_name = peewee.CharField()

    class Meta:
        database = pg_db
        db_table = 'user'

User.create_table()

class Store(peewee.Model):
    """ Class to define the Store table."""
    stores_tags = peewee.TextField(primary_key=True)

    class Meta:                
        database = pg_db
        db_table = 'store'

Store.create_table()

class Category(peewee.Model):
    """ Class to define the Category table."""    
    categories = peewee.TextField(primary_key=True)

    class Meta:                
        database = pg_db
        db_table = 'category'

Category.create_table()

class Product(peewee.Model):
    """ Class to define the Product table."""
    _id = peewee.BigIntegerField(primary_key=True)
    categories = peewee.ForeignKeyField(Category, backref='product')
    ingredients_text_fr = peewee.TextField()
    nutrition_grade_fr = peewee.CharField()
    product_name_fr = peewee.TextField()
    stores_tags = peewee.ForeignKeyField(Store, backref='product')
    url = peewee.TextField()

    class Meta:                
        database = pg_db
        db_table = 'product'

Product.create_table()

class History(peewee.Model):
    """ Class to define the History table."""
    user = peewee.ForeignKeyField( User, backref='history')
    chosen_product = peewee.ForeignKeyField( Product, backref='history')
    remplacement_product = peewee.ForeignKeyField(Product, backref='history')

    class Meta:
        primary_key = peewee.CompositeKey('user', 'chosen_product')                
        database = pg_db
        db_table = 'history'

History.create_table()        

class ProductCategory(peewee.Model):
    """ Class to define the Product category table."""
    product = peewee.ForeignKeyField ( Product, backref='product_category')
    category = peewee.ForeignKeyField ( Category, backref='product_category')

    class Meta:
        primary_key = peewee.CompositeKey('product', 'category')                
        database = pg_db
        db_table = 'product_category'

ProductCategory.create_table()

class ProductStore(peewee.Model):
    """ Class to define the Product Store table."""
    product = peewee.ForeignKeyField( Product, backref='product_store')
    store = peewee.ForeignKeyField(Store, backref='product-store')

    class Meta:
        primary_key = peewee.CompositeKey('product', 'store')                
        database = pg_db
        db_table = 'product_store'

ProductStore.create_table()

"""
Iport the products from download_products
"""
cat = DataFiles.categories
stg = DataFiles.stores_tags  
pr = DataFiles.products

"""
Insert all products in database
"""
query1 = Category.insert_many(cat)
query2 = Store.insert_many(stg)  
query3 = Product.insert_many(pr)
query1.execute()
query2.execute()        
query3.execute()
        
