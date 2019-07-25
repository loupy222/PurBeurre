import peewee

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
    s_name = peewee.CharField(primary_key=True)

    class Meta:                
        database = pg_db
        db_table = 'store'

Store.create_table()

class Category(peewee.Model):
    """ Class to define the Category table."""
    c_name = peewee.CharField(primary_key=True)

    class Meta:                
        database = pg_db
        db_table = 'category'

Category.create_table()

class Product(peewee.Model):
    """ Class to define the Product table."""
    id = peewee.PrimaryKeyField()
    p_name =  peewee.CharField()
    store = peewee.ForeignKeyField(Store, to_field='s_name', backref='product')
    url_link = peewee.CharField()
    category = peewee.ForeignKeyField(Category, to_field = 'c_name', backref='product')
    ingredients = peewee.CharField()
    nutriscore = peewee.IntegerField()

    class Meta:                
        database = pg_db
        db_table = 'product'

Product.create_table()

class History(peewee.Model):
    """ Class to define the History table."""
    user = peewee.ForeignKeyField( User, field = 'id', backref='history')
    products = peewee.ForeignKeyField( Product, field= 'id', backref='history')

    class Meta:
        primary_key = peewee.CompositeKey('user', 'products')                
        database = pg_db
        db_table = 'history'

History.create_table()        

class ProductCategory(peewee.Model):
    """ Class to define the Product category table."""
    product = peewee.ForeignKeyField ( Product, field = 'id', backref='product_category')
    category = peewee.ForeignKeyField ( Category, field = 'c_name', backref='product_category')

    class Meta:
        primary_key = peewee.CompositeKey('product', 'category')                
        database = pg_db
        db_table = 'product_category'

ProductCategory.create_table()

class ProductStore(peewee.Model):
    """ Class to define the Product Store table."""
    product = peewee.ForeignKeyField( Product, field = 'id', backref='product_store')
    store = peewee.ForeignKeyField(Store, field='s_name', backref='product-store')

    class Meta:
        primary_key = peewee.CompositeKey('product', 'store')                
        database = pg_db
        db_table = 'product_store'

ProductStore.create_table()   

