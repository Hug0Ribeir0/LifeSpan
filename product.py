import sys
from unittest import case
from categories import category

class Product:
    def __init__(self, p_name, p_category, p_price, p_desc) -> None:
        self.name = p_name
        self.id = None
        self.category = p_category
        self.cost = float(p_price)
        self.description = p_desc

    def show(self):
        print(f'{self.name} {self.category} {self.cost} {self.description} {self.id}')

    def set_id(self, p_id):
        self.id = p_id

    def change_product(self, p_name=None, p_category=None, p_price=None, p_desc=None):
        if p_name is not None:
            self.name = p_name
        if p_category is not None:
            self.category = p_category
        if p_price is not None:
            self.cost = p_price
        if p_desc is not None:
            self.description = p_desc
