import requests, json
from dataclasses import dataclass
from clear_data import CleanFile
import pprint
@dataclass
class DataFiles:
    """
    Class allowing to download and filter the products to be inserted in the Data Base.
    """
    snacks = list
    pizza = list
    drinks = list
    cheese = list
    pasta = list
    products = list
    categories = list
    stores_tags = list

    """
    Modul to download, clean and parse the products-file.
    """
    link1 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=snacks&page_size=100&search_simple=1&action=process&page=2&json=1"
    link2 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=pizza&page_size=100&search_simple=1&action=process&page=2&json=1"
    link3 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=boisons&page_size=100&search_simple=1&action=process&page=2&json=1"
    link4 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=fromages&page_size=100&search_simple=1&action=process&page=2&json=1"
    link5 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=pates&page_size=100&search_simple=1&action=process&page=2&json=1"

    print( "Program started let's do some work now!")
    r = requests.get(link1)
    snacks = json.loads(r.content)# rec the data in a variable
    print("We have now 1000 products downloaded!")

    r = requests.get(link2)
    pizzas = json.loads(r.content)# rec the data in a variable
    print("We have now 2000 products downloaded!")

    r = requests.get(link3)
    drinks = json.loads(r.content)
    print("We have now 3000 products downloaded!")

    r = requests.get(link4)
    cheese = json.loads(r.content)
    print("We have now 4000 products downloaded!")

    r = requests.get(link5)
    pasta = json.loads(r.content)
    print("We have now 5000 products downloaded! Now let's clean them ;-) !")


    snacks = CleanFile.clean_data(snacks) # cleanup the data
    print("We have now ", len( snacks ), "products downloaded and cleaned!")

    pizzas = CleanFile.clean_data(pizzas)
    l0 = snacks + pizzas
    print("We have now", len( l0 ), "products downloaded and cleaned!")

    drinks = CleanFile.clean_data(drinks)
    l1 = l0 + drinks
    print("We have now", len( l1 ), "products downloaded and cleaned!")

    cheese = CleanFile.clean_data(cheese)
    l2 = l1 + cheese
    print("We have now", len( l2 ), "products downloaded and cleaned!")

    pasta = CleanFile.clean_data(pasta)
    l3 = l2 + pasta
    print("We have now", len( l3 ), "all products downloaded, and cleaned!")

    products = l3
    products = CleanFile.clean_products(products)
    print("After a hard cleaning job we have", len(products), "let's put them in the Data_Base!")

    categories = CleanFile.select_categories(products)
    print("We have ", len(categories),"categories!")

    stores_tags = CleanFile.select_stores_tags(products)
    print("Wee have ", len(stores_tags),"stores!")

    _id_and_stores = CleanFile.select_id_and_stores_tags(products)
    pprint.pprint(_id_and_stores)

if __name__ == "__main__":
    pass