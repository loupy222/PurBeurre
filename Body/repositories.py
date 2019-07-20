import psycopg2

con = psycopg2.connect(database="Pure_Beurre", user="loupy", host="localhost", password="bcxau9p^^123")


class UserRepository:
    pass

class HistoryRepository:
    pass

class ProductRepository:
    pass

class CategoryRepository:
    pass

class StoreRepository:
    pass

con.close()