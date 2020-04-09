class ShoppingCart():
    items_present_in_cart = {}
    def __init__(self,customer_id):
        self.customer_id = customer_id

    def add_item(self,product,price):
        if product not in self.items_present_in_cart:
            self.items_present_in_cart[product]=price
            print(product+" Added")
        else:
            print("{} is already present".format(product))


    def remove_item(self,product):
        if product in self.items_present_in_cart:
            self.items_present_in_cart.pop(product)
            print(product+" Removed")
        else:
            print("{} not present in the cart".format(product))




