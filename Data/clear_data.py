import json
from dataclasses import dataclass

@dataclass
class CleanFile:

    
    def clean_data (file):
        products = file["products"]
    
        wanted_labels = ["_id",
        "product_name_fr",
        "stores_tags",
        "url",
        "categories",
        "ingredients_text_fr",
        "nutrition-score"]

        processed_products = []

        for product in products:
            current_product = {}

            for p_label, p_value in product.items():

                if p_label in wanted_labels:
                    current_product.update({p_label: p_value})

            processed_products.append(current_product)
        file = processed_products
        return file

