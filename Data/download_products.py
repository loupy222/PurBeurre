import requests, json
from dataclasses import dataclass
from clear_data import CleanFile

@dataclass
class DownloadFiles:
    snacks = list
    pizza = list
    water = list
    cheese = list
    pasta = list
    products = list


link1 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=snacks&page_size=1000&search_simple=1&action=process&page=2&json=1"
link2 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=pizza&page_size=1000&search_simple=1&action=process&page=2&json=1"
link3 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=eau&page_size=1000&search_simple=1&action=process&page=2&json=1"
link4 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=fromages&page_size=1000&search_simple=1&action=process&page=2&json=1"
link5 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=pates&page_size=1000&search_simple=1&action=process&page=2&json=1"

r = requests.get(link1)

snacks = json.loads(r.content)

snacks = CleanFile.clean_data(snacks)


r = requests.get(link2)

pizza = json.loads(r.content)

pizza = CleanFile.clean_data(pizza)


r = requests.get(link3)

water = json.loads(r.content)

water = CleanFile.clean_data(water)


r = requests.get(link4)

cheese = json.loads(r.content)

cheese = CleanFile.clean_data(cheese)


r = requests.get(link5)

pasta = json.loads(r.content)

pasta = CleanFile.clean_data(pasta)


products = snacks + pizza + water + cheese + pasta
