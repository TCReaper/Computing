###################################################################
# Implementation of Code in this section
# Hint: round(float, 2) will return a float with 2 d.p.
# Hint: "{:>12.2f}".format(float) will format float in 12 blank
#        placeholders, align to the right, formatted to 2 d.p.
###################################################################




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

# test_function_5_1()


def test_function_5_2():
    print("Begin test function 5.2\n")

    sm = StoreManager(g_list)
    sold_item_list = [("Spoon", 2), ("Fork", 3)]
    sm.sell_list(sold_item_list)

    print()
    sm.stock_check()

    print("\nEnd of test function 5.2\n")

# test_function_5_2()
