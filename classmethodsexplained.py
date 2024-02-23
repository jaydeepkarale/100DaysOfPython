class Item:
    # Class variable to store product details
    product_details = {
        'P001': {'name': 'Laptop', 'price': 999.99, 'quantity_in_stock': 50},
        'P002': {'name': 'Smartphone', 'price': 499.99, 'quantity_in_stock': 100},
        # ... more products
    }

    def __init__(self, name, price, quantity_in_stock):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    @classmethod
    def from_product_code(cls, product_code):
        # Fetch product details based on the product code
        default_info = {'name': 'Product Not Found', 'price': 0.0, 'quantity_in_stock': 0}
        product_info = cls.product_details.get(product_code, default_info)
        return cls(product_info['name'], product_info['price'], product_info['quantity_in_stock'])

class ShoppingCartItem(Item):
    def dummy_method(self):
        print("This is a dummy method in ShoppingCartItem")

# Usage
laptop = Item("Laptop", 999.99, 50)
smartphone_from_code = Item.from_product_code("P002")  # Using the alternate constructor

print(laptop.name, laptop.price, laptop.quantity_in_stock)
# Output: Laptop 999.99 50

print(smartphone_from_code.name, smartphone_from_code.price, smartphone_from_code.quantity_in_stock)
# Output: Smartphone 499.99 100

# Inheriting class using the dummy method
shopping_cart_item = ShoppingCartItem.from_product_code("P001")  # Using the alternate constructor
shopping_cart_item.dummy_method()  # Using the dummy method
