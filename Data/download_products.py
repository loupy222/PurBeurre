import requests, json

link1 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=Snacks&page_size=1000&search_simple=1&action=process&page=2&json=1"
link2 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=Pizza&page_size=1000&search_simple=1&action=process&page=2&json=1"
link3 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=Eau&page_size=1000&search_simple=1&action=process&page=2&json=1"
link4 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=Fuits&page_size=1000&search_simple=1&action=process&page=2&json=1"
link5 = "https://fr.openfoodfacts.org/cgi/search.pl?%22category=Pates&page_size=1000&search_simple=1&action=process&page=2&json=1"

r = requests.get(link1)

Snacks = json.loads(r.content)

with open('Snacks.json', 'w') as f:
    json.dump(Snacks, f)

r = requests.get(link2)

Pizza = json.loads(r.content)

with open('Pizza.json', 'w') as f:
    json.dump(Pizza, f)

r = requests.get(link3)

Eau = json.loads(r.content)

with open('Eau.json', 'w') as f:
    json.dump(Eau, f)

r = requests.get(link4)

Fruits = json.loads(r.content)

with open('Fruits.json', 'w') as f:
    json.dump(Fruits, f)

r = requests.get(link5)

Pates = json.loads(r.content)

with open('Pates.json', 'w') as f:
    json.dump(Pates, f)