from dataclasses import dataclass

@dataclass
class User:
    name: str

@dataclass
class Product:
    Bar_code: int
    Name: str
    Url_link: str
    Ingredients: list
    Nutriscore: int
    Categories: list
    Stores: list

@dataclass
class Category:
    Name: str
    Products: list

@dataclass
class Store:
    Name: str
    Products: list