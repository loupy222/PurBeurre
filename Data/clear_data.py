from dataclasses import dataclass
from collections import OrderedDict

@dataclass
class CleanFile:
    """
    Class to filter the data.
    """

    def clean_data (file):
        """
        Clean the downloaded file and choose juste that wee need
        """
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
                        if p_value != None or "null":       
                            current_product.update({p_label: p_value})
                            # add to current_product if key and value are present

            if len(current_product) == 7:
                o_current_product = OrderedDict(sorted(current_product.items(), key=lambda t: t[0]))
                if o_current_product not in processed_products: 
                    processed_products.append(o_current_product)
                    
        return processed_products #return cleaned file

    def clean_products(file):
        """
        Clean the main file once again.
        """
        products = file
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
                        if p_value != None or "null":      
                            current_product.update({p_label: p_value})
                            # add to current_product if key and value are present

            if len(current_product) == 7:
                o_current_product = OrderedDict(sorted(current_product.items(), key=lambda t: t[0]))
                if o_current_product not in processed_products: 
                    processed_products.append(o_current_product)
        return processed_products #return cleaned file
    
    def select_categories(file):
        """
        Search and records all categories for insert in data_base.
        """
        products = file
        processed_categories = []
        for product in products:
            values_list = []
            current_categorie = {}
            for p_label, p_value in product.items():
                if p_label == "categories":
                    values_list = p_value.split(',')
                    for i in values_list:
                        current_categorie.update({p_label: i})
            if current_categorie not in processed_categories:
                processed_categories.append(current_categorie)
        return processed_categories

    def select_stores_tags(file):
        """
        Search and records all store_tags for insert in data_base.
        """
        products = file
        processed_stores_tags = []
        for product in products:
            current_stores_tags = {}
            for p_label, p_value in product.items():
                if p_label == "stores_tags":
                    for i in p_value:
                        current_stores_tags.update({p_label: i})
            if current_stores_tags not in processed_stores_tags:
                processed_stores_tags.append(current_stores_tags)
        return processed_stores_tags


    """def select_id_and_stores_tags(file):
        """"""
        Search and records all store_tags for insert in data_base.
        """"""
        products = file
        processed_stores_tags = []
        for product in products:
            current_stores_tags = {}
            for p_label, p_value in product.items():
                if p_label == "_id":
                    current_stores_tags.update({p_label: p_value})
                if p_label == "stores_tags":
                    for v in p_value:
                        current_stores_tags.update({p_label: v})
                        print(current_stores_tags)
                        processed_stores_tags.append(current_stores_tags)
        return processed_stores_tags""" 