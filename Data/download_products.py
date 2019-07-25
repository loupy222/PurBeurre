import requests, json
from dataclasses import dataclass
from clear_data import CleanFile

@dataclass
class DownloadFiles:
    """
    Class allowing to download and filter the products to be inserted in the Data Base.
    """
    snacks = list
    pizza = list
    water = list
    cheese = list
    pasta = list
    products = list


link1 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=snacks&page_size=1000&search_simple=1&action=process&page=2&json=1"
link2 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=pizza&page_size=1000&search_simple=1&action=process&page=2&json=1"
link3 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=boisons&page_size=1000&search_simple=1&action=process&page=2&json=1"
link4 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=fromages&page_size=1000&search_simple=1&action=process&page=2&json=1"
link5 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=pates&page_size=1000&search_simple=1&action=process&page=2&json=1"

print( "Program started let's do some work now")
r = requests.get(link1)

snacks = json.loads(r.content)# rec the data in a variable
print("Download finished successfully!")
snacks = CleanFile.clean_data(snacks) # cleanup the data
print("We have now ", len( snacks ), "downloaded and cleaned!!!")

r = requests.get(link2)

pizza = json.loads(r.content)
print("Download finished successfully!")
pizza = CleanFile.clean_data(pizza)
l0 = snacks + pizza
print("We have now ", len( l0 ), "downloaded and cleaned!!!")


r = requests.get(link3)

drinks = json.loads(r.content)
print("Download finished successfully!")
drinks = CleanFile.clean_data(drinks)
l1 = l0 + drinks
print("We have now ", len( l1 ), "downloaded and cleaned!!!")

r = requests.get(link4)

cheese = json.loads(r.content)
print("Download finished successfully!")
cheese = CleanFile.clean_data(cheese)
l2 = l1 + cheese
print("We have now ", len( l2 ), "downloaded and cleaned!!!")

r = requests.get(link5)

pasta = json.loads(r.content)
print("Download finished successfully!")
pasta = CleanFile.clean_data(pasta)
l3 = l2 + pasta
print("We have now ", len( l3 ), "downloaded, and cleaned! Now you can store it ;-) !!!")

