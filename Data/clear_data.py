import json
from dataclasses import dataclass
from collections import OrderedDict

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
        "nutrition_grade_fr"] #list of the labels to search, test and add to the new list
        
        print ( "Let's do some clean-up job!")
        processed_products = [] 

        for product in products:# the list contains dictionaries
            current_product = {}
            o_current_product = {}
            for p_label, p_value in product.items(): #test if the labels and values are in the dictionary
                if p_label in wanted_labels:
                    if len(p_value) != 0:      
                        current_product.update({p_label: p_value})
                        # add to current_product if key and value are present

            if len(current_product) == 7:
                o_current_product = OrderedDict(sorted(current_product.items(), key=lambda t: t[0]))
                if current_product not in processed_products: 
                    processed_products.append(current_product)
                    
        return processed_products #return cleaned file