###################################################################
# Implementation of Code in this section
# Hint: round(float, 2) will return a float with 2 d.p.
# Hint: "{:>12.2f}".format(float) will format float in 12 blank
#        placeholders, align to the right, formatted to 2 d.p.
###################################################################


class Grocery(object):
    """class Grocery inherit from class object"""

    # initializer for class Grocery
    def __init__(self, title, cost, price, stock):
        self._title = title
        self._cost = cost
        self._price = price
        self._stock = stock
        self._gst = 1.07
        self._promotion = 1

    # Mutator Functions
    def set_title(self, new_title):
        self._title = new_title

    def set_cost(self, new_cost):
        self._cost = new_cost

    def set_price(self, new_price):
        self._price = new_price

    # Accessor Functions
    def get_title(self):
        return self._title

    def get_cost(self):
        return self._cost

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    # Functions
    def update_stock(self, change_in_stock):
        self._stock += change_in_stock

    def calculate_final_price(self):
        return round(self._price * self._gst, 2)

    # String Representation of Class Grocery
    def __str__(self):
        result = "{:<20} | ${:>6} | ${:>6} | {:>6} | ${:>12}".format(self._title,self._cost, self._price, self._stock,
            self.calculate_final_price())

        return result


class ElectricalAppliance(Grocery):
    """class ElectricalAppliance inherit from class Grocery"""

    # initializer for class ElectricalAppliance
    def __init__(self, title, cost, price, stock, power):
        super().__init__(title, cost, price, stock)
        self._power = power

    # Accessor Functions
    def get_power(self):
        return self._power

    # Function
    def calculate_final_price(self):
        if self._power <= 10:
            self._promotion = 0.8
        return round(super().calculate_final_price() * self._promotion, 2)


class Cigarette(Grocery):
    """class Cigarette inherit from class Grocery"""

    # initializer for class Cigarette
    def __init__(self, title, cost, price, stock, nicotine_content):
        super().__init__(title, cost, price, stock)
        self._nicotine_content = nicotine_content
        self._tax = 1.6

    # Accessor Functions
    def get_nicotine_content(self):
        return self._nicotine_content

    # Function
    def calculate_final_price(self):
        return round(super().calculate_final_price() * self._tax, 2)


class Alcohol(Grocery):
    """class Alcohol inherit from class Grocery"""

    # initializer for class Alcohol
    def __init__(self, title, cost, price, stock, type):
        super().__init__(title, cost, price, stock)
        self._type = type
        if type == "wine":
            self._tax = 1.6
        elif type == "beer":
            self._tax = 1.2
        else:
            self._tax = 1

    # Accessor Functions
    def get_type(self):
        return self._type

    # Function
    def calculate_final_price(self):
        return round(super().calculate_final_price() * self._tax, 2)


class StoreManager():
    def __init__(self, curr_item_list):
        self._curr_item_list = curr_item_list

    def sell_item(self, sold_item):
        title = sold_item[0]
        sold_quantity = sold_item[1]

        for item in self._curr_item_list:
            if item.get_title() == title:
                item.update_stock(-1 * sold_quantity)
                final_price = item.calculate_final_price()
                sub_total = round(final_price * sold_quantity, 2)

                print("{:<20} |$ {:>12.2f} | {:>15} |$ {:>12}".format(item.get_title(), final_price, sold_quantity, sub_total))

                return sub_total

    def sell_item_list(self, sold_item_list):
        total = 0

        print("{:-^70}".format("Receipt"))
        print("{:<20} |  {:>12} | {:>15} |  {:>12}".format("Title", "Final Price", "Quantity Sold", "Subtotal"))
        print("{:-^70}".format(""))

        for tuple in sold_item_list:
            total += self.sell_item(tuple)
        print("{:-^70}".format(""))
        print("Total: ${:.2f}".format(total))

    def stock_check(self):
        print("{:-^54}".format("Stock Check"))
        print("{:<20} |  {:>12} | {:>15}".format("Title", "Unit Cost", "Quantity Left"))
        print("{:-^54}".format(""))

        for item in self._curr_item_list:
            if item.get_stock() < 5:
                print("{:<20} |$ {:>12.2f} | {:>15}".format(item.get_title(), item.get_cost(), item.get_stock()))


####################################################
# Please do not modify the code below
####################################################


def initialise_data():
    g1 = Grocery("Spoon", 1.5, 2.5, 15)
    g2 = Grocery("Fork", 1.7, 3.0, 5)
    g3 = Grocery("Shampoo", 5.2, 11, 11)
    g4 = Grocery("Power Cable", 6.5, 15, 12)

    ea1 = ElectricalAppliance("Normal Light Bulb 01", 2, 3, 3, 25)
    ea2 = ElectricalAppliance("Normal Light Bulb 02", 2.5, 4, 6, 30)
    ea3 = ElectricalAppliance("LED Light Bulb", 6, 10, 9, 5)
    ea4 = ElectricalAppliance("Desk Light", 30, 50, 2, 50)
    ea5 = ElectricalAppliance("LED Desk Light", 40, 60, 15, 10)

    c1 = Cigarette("Marlboro Red", 27.65, 35, 15, 0.7)
    c2 = Cigarette("Bomond Blue", 12.10, 15, 12, 0.7)
    c3 = Cigarette("Camel Filters", 23.38, 30, 23, 0.6)
    c4 = Cigarette("Yun Yan", 16.5, 23, 4, 0.65)

    a1 = Alcohol("Barefoot", 55, 86, 3, "wine")
    a2 = Alcohol("Great Wall", 45, 80, 5, "wine")
    a3 = Alcohol("Hardys", 57, 90, 6, "wine")
    a4 = Alcohol("Coors Light", 15, 27, 13, "beer")
    a5 = Alcohol("Tsingtao", 10, 20, 7, "beer")

    return [g1, g2, g3, g4, ea1, ea2, ea3, ea4, ea5, c1, c2, c3, c4, a1, a2, a3, a4, a5]

g_list = initialise_data()


def test_function_5_1():
    print("Begin test function 5.1\n")

    print("{:-^65}".format("Current Grocery List"))
    print("{:<20} |  {:>6} |  {:>6} | {:>6} |  {:>12}".format("Title", "Cost", "Price", "Stock", "Final Price"))
    print("{:-^65}".format(""))

    for g in g_list:
        print(g)

    print("\nEnd of test function 5.1\n")

test_function_5_1()


def test_function_5_2():
    print("Begin test function 5.2\n")

    sm = StoreManager(g_list)
    sold_item_list = [("Spoon", 2), ("Fork", 3)]
    sm.sell_item_list(sold_item_list)

    print()
    sm.stock_check()

    print("\nEnd of test function 5.2\n")

test_function_5_2()