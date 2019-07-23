import json
from dataclasses import dataclass

@dataclass
class CleanFile:
    """
    Class to filter the data.
    """

    def clean_data (file):
        products = file["products"] # reach to the list os the products
    
        wanted_labels = ["_id",
        "product_name_fr",
        "stores_tags",
        "url",
        "categories",
        "ingredients_text_fr",
        "nutrition-score"] #list of the labels to search, test and add to the new list

        processed_products = [] 

        for product in products:# the list contains dictionaries
            current_product = {}

            for p_label, p_value in product.items(): #test if the labels and values are in the dictionaru

                if p_label in wanted_labels:# test if the labels are in the dictionaru
                    if p_value != [] or "" "":# test if values exists                                          
                        current_product.update({p_label: p_value})# add if data is present and not blanc

            processed_products.append(current_product)# add result to the new list
        file = processed_products
        return file #return file

