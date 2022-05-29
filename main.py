import categories
from operator import ne
from unicodedata import category
from product import Product
from categories import category


def add_product():
    p_name = input('Product name: ')


new_product = Product('Logitech Pro Mouse', category.IT, 79.99, 'Logitech Mouse, the previous started malfunction')

new_product.show()

#new_product.change_product(p_category=category.gaming)

new_product.show()

#new_product.change_product(p_name='Mouse Log', p_price=80)

#new_product.show()

print('test ended')