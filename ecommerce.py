class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventory, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print('We are out of stock!')
        else:
            print("We don't have that product!")

    def print_purchases(self):
        print("The customer has purchased")
        for item in self.purchases:
            print(item.name)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product] += quantity

    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key.name + ':' + str(value))
        print()


customer = Customer('Joe', 'joe@gmail.com')
print(customer.name)
print(customer.email)

apple_watch = Product('Apple Watch', 299)
print(apple_watch.name)
print(apple_watch.price)

mac = Product('Mac', 1999)
print(mac.name)
print(mac.price)

inventory = Inventory()
inventory.add_product(apple_watch, 100)
inventory.print_inventory()
inventory.add_product(mac, 498)

inventory.print_inventory()
customer.purchase(inventory, apple_watch)
customer.purchase(inventory, mac)
inventory.print_inventory()
customer.print_purchases()
