import json


with open ("Eau.json") as f:
    Eau = json.load(f)
Products = Eau['products']

"""print(len(Products))
print(Products[1].keys())"""
