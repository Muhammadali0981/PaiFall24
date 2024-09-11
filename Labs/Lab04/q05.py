class Resturant:
    def __init__(self, menu_items, booked_table, costumer_order):
        self.menu_items = menu_items
        self.booked_table = booked_table
        self.costumer_order = costumer_order

    def add_menu_item(self):
        name, price = input("enter name and price of item ").split()
        self.menu_items[name] = price

    def book_table(self):
        cname, ppl = input("enter name and number of people ").split()
        self.booked_table[cname] = ppl

    def take_order(self):
        name, order = input("enter name and order ").split()
        self.costumer_order.append((name, order))

    def print_menu(self):
        print(self.menu_items)

    def print_orders(self):
        print(self.costumer_order)

    def print_table(self):
        print(self.booked_table)

r1 = Resturant({"briyani": 220, "chai" : 60, "askari cola" : 65, "pasta": 500 }, {}, [])
r1.add_menu_item()
r1.book_table()
r1.take_order()
r1.print_menu()
r1.print_orders()
r1.print_table()