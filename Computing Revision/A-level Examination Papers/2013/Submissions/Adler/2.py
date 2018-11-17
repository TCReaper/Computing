#First line of file, after being split with "

##['EmployeeCode(1) = ', 'L001', ' : Surname(1) = ', 'Pollard', \
##' : EmployeeCode(2) = ', 'L002', ' : Surname(2) = ', 'Wills', '']

#Index 1 is the first employee code, 3 is name for that person
#Index 5 is the second employee code, 7 is name for that person

SearchItem = input("Item to search: ")

def detect_type(SearchItem):
    #returns 0 if surname, 1 if employee code, -1 if invalid for both
    if SearchItem.isalpha():
        return 0
    
    if len(SearchItem) == 4 \
       and SearchItem[0].isalpha() \
       and SearchItem[1:].isdigit():
        return 1
    return -1
    
def get_file_data(): #returns ARRAY of ARRAYS:[ID, Surname]
    file_data = []
    f = open("EMPLOYEEDATA.TXT")
    for line in f:
        temp = line.strip().split('"')
        file_data.append([temp[1], temp[3]])
        file_data.append([temp[5], temp[7]])        
    f.close()
    return file_data

##def search_by_surname():
##    while True:
##        target = input("Enter a valid Surname: ")
##        if target.isalpha():
##            return search(target, 1)[0]
##        print("Invalid Surname! Try again.")
##
##def search_by_employee_id():
##    while True:
##        target = input("Enter a valid Employee ID: ")
##        if len(target) == 4:
##            if target[0].isalpha() and target[1:].isdigit():
##                return search(target, 0)[1]
##        print("Invalid Employee ID! Try again.") 

def search(target, index):
    file_data = get_file_data()
    for i in range(len(file_data)):
        if file_data[i][index].upper() == target.upper():
            return file_data[i]
    return ['Surname Not Found', 'Employee ID Not Found'] #when not found



ItemType = detect_type(SearchItem)
if ItemType == 0: #surname
    print(search(SearchItem, 0)[1])
elif ItemType == 1: #employee code
    print(search(SearchItem, 1)[0])
else: #ItemType = -1
    print("Invalid input!")
