print("Task 2.1 - Evidence 11")
def test1():
    #If your BST structure is not defined by a class, you can change the way these functions are called.
    b1 = createBST()
    print(b1.findTotalCost())
    print(b1.findWorkshopsById("1001278B"))
    print(b1.findWorkshopsById("1019563R"))
    print(b1.findWorkshopsById("3161202Y"))
    print(b1.findWorkshopsById("5095845H"))
    print(b1.findWorkshopsById("9965997Y"))
    print(b1.findWorkshopsById("9998622F"))
    print(b1.findIdsByWorkshop('Diabetes 101'))
    print(b1.findIdsByWorkshop('The Truth About Carbs'))
    print(b1.findIdsByWorkshop('Nutrition Nuts And Bolts'))
    print(b1.findIdsByWorkshop('Yoga With Yoyo'))
#test1()


print("Task 2.2 - Evidence 12")
def menu_display():
    print("1) Read file to generate BST")
    print("2) Find workshop(s) by user ID.")
    print("3) Find user ID(s) by workshop.")
    print("4) Display users in order.")
    print("5) Total cost.")
    print("6) Quit.")

def menu():
    pass
