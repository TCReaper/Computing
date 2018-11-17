def read_input_file(filename, lst):
    with open (filename,'r') as f:
        line = f.readline()
        while line:
            if line[-1]=='\n':
                lst.append(line[:-1])
            else:
                lst.append(line)
            line = f.readline()
    f.close()

#The dict provided below is for you to use if you cannot complete task 1.
solution_dict = {'Rufus Schuck': {'EL': ['C', 'B'], 'CL': ['C', 'C'], 'Math': ['C', 'E'], 'Bio': ['B', 'F']},
'Ione Wolfe': {'EL': ['D', 'C'], 'CL': ['D', 'C'], 'Math': ['F', 'C'], 'Phy': ['B', 'B'], 'Bio': ['C', 'C'], 'Chem': ['B', 'C']},
'Hillary Curl': {'EL': ['B', 'D'], 'CL': ['C', 'B'], 'Math': ['E', 'A'], 'Phy': ['B', 'E'], 'Bio': ['C', 'C'], 'Chem': ['E', 'C']},
'Juli Barnhill': {'EL': ['E', 'C'], 'CL': ['C', 'A'], 'Math': ['D', 'E'], 'Bio': ['B', 'C'], 'Chem': ['E', 'D']},
'Tashia Bowen': {'EL': ['B', 'B'], 'CL': ['B', 'A'], 'Math': ['A', 'A'], 'Bio': ['D', 'C']},
'Marguerita Mciver': {'EL': ['B', 'A'], 'CL': ['E', 'D'], 'Math': ['F', 'E'], 'Phy': ['E', 'B']},
'Sharie Schall': {'EL': ['B', 'C'], 'CL': ['E', 'A'], 'Math': ['F', 'C'], 'Phy': ['D', 'A'], 'Chem': ['A', 'E']},
'Paris Curington': {'EL': ['C', 'E'], 'CL': ['E', 'C'], 'Math': ['B', 'D'], 'Phy': ['B', 'A'], 'Bio': ['A', 'F'], 'Chem': ['C', 'C']},
'Ashely Faye': {'EL': ['C', 'C'], 'CL': ['B', 'E'], 'Math': ['C', 'C'], 'Chem': ['B', 'D']},
'Elvia Dubrey': {'EL': ['B', 'A'], 'CL': ['C', 'B'], 'Math': ['A', 'E'], 'Phy': ['C', 'E'], 'Bio': ['C', 'B'], 'Chem': ['F', 'E']},
'Terrence Shannon': {'EL': ['C', 'C'], 'CL': ['C', 'F'], 'Math': ['D', 'B'], 'Phy': ['E', 'A'], 'Bio': ['C', 'F'], 'Chem': ['C', 'C']},
'Carolann Kintner': {'EL': ['B', 'A'], 'CL': ['B', 'B'], 'Math': ['D', 'E'], 'Phy': ['B', 'B']},
'So Atkins': {'EL': ['E', 'C'], 'CL': ['C', 'D'], 'Math': ['F', 'D'], 'Phy': ['B', 'A'], 'Chem': ['C', 'C']},
'Kathlene Collar': {'EL': ['D', 'C'], 'CL': ['C', 'E'], 'Math': ['A', 'E'], 'Phy': ['C', 'E'], 'Bio': ['B', 'A'], 'Chem': ['C', 'D']},
'Luanne Lett': {'EL': ['A', 'C'], 'CL': ['E', 'F'], 'Math': ['B', 'C'], 'Phy': ['E', 'B'], 'Chem': ['D', 'D']},
'Ola Markell': {'EL': ['D', 'B'], 'CL': ['E', 'C'], 'Math': ['F', 'B'], 'Phy': ['A', 'C'], 'Bio': ['D', 'D']},
'Claudette Bode': {'EL': ['C', 'D'], 'CL': ['D', 'A'], 'Math': ['A', 'D'], 'Phy': ['A', 'D'], 'Bio': ['D', 'C']},
'Lashawna Meals': {'EL': ['A', 'D'], 'CL': ['C', 'D'], 'Math': ['E', 'F'], 'Chem': ['C', 'A']},
'Angle Linck': {'EL': ['C', 'A'], 'CL': ['E', 'D'], 'Math': ['C', 'E'], 'Phy': ['D', 'E'], 'Chem': ['D', 'D']},
'Toney Mcnab': {'EL': ['C', 'A'], 'CL': ['C', 'A'], 'Math': ['C', 'B'], 'Chem': ['B', 'D']},
'Hertha Dossantos': {'EL': ['F', 'B'], 'CL': ['B', 'C'], 'Math': ['C', 'E'], 'Chem': ['E', 'C']},
'Jalisa Stoudemire': {'EL': ['B', 'A'], 'CL': ['D', 'C'], 'Math': ['C', 'B'], 'Phy': ['C', 'A'], 'Bio': ['E', 'D'], 'Chem': ['D', 'C']},
'Johnna Lecuyer': {'EL': ['F', 'F'], 'CL': ['A', 'E'], 'Math': ['D', 'C'], 'Bio': ['D', 'C']},
'Grazyna Kitzman': {'EL': ['B', 'C'], 'CL': ['C', 'E'], 'Math': ['F', 'D'], 'Phy': ['C', 'D'], 'Bio': ['D', 'B'], 'Chem': ['C', 'E']},
'Phyliss Rolen': {'EL': ['B', 'F'], 'CL': ['C', 'E'], 'Math': ['D', 'C'], 'Chem': ['B', 'D']},
'Shaunda Sieg': {'EL': ['C', 'D'], 'CL': ['C', 'D'], 'Math': ['A', 'C'], 'Bio': ['C', 'E']},
'Abdul Boland': {'EL': ['E', 'E'], 'CL': ['B', 'E'], 'Math': ['B', 'D'], 'Bio': ['D', 'B']},
'Lai Lazard': {'EL': ['C', 'A'], 'CL': ['C', 'D'], 'Math': ['D', 'F'], 'Bio': ['A', 'D']},
'Chadwick Griffin': {'EL': ['E', 'F'], 'CL': ['D', 'F'], 'Math': ['B', 'E'], 'Chem': ['D', 'D']},
'Jaye Galle': {'EL': ['B', 'D'], 'CL': ['C', 'C'], 'Math': ['D', 'B'], 'Phy': ['C', 'C'], 'Bio': ['C', 'C'], 'Chem': ['A', 'C']},
'Virgilio Britt': {'EL': ['C', 'D'], 'CL': ['A', 'D'], 'Math': ['B', 'E'], 'Bio': ['E', 'A'], 'Chem': ['C', 'D']},
'Lanita Sciortino': {'EL': ['B', 'A'], 'CL': ['C', 'D'], 'Math': ['C', 'B'], 'Chem': ['E', 'D']},
'See Borne': {'EL': ['C', 'A'], 'CL': ['E', 'B'], 'Math': ['A', 'B'], 'Phy': ['F', 'E'], 'Chem': ['F', 'E']},
'Laverna Halpern': {'EL': ['A', 'C'], 'CL': ['C', 'E'], 'Math': ['C', 'C'], 'Phy': ['C', 'E'], 'Chem': ['B', 'E']},
'Russell Gillison': {'EL': ['C', 'A'], 'CL': ['A', 'F'], 'Math': ['A', 'C'], 'Bio': ['C', 'C']},
'Joella Wessner': {'EL': ['C', 'C'], 'CL': ['B', 'C'], 'Math': ['C', 'E'], 'Chem': ['C', 'E']},
'Fredricka Gormley': {'EL': ['C', 'D'], 'CL': ['C', 'D'], 'Math': ['C', 'D'], 'Phy': ['B', 'B']},
'Marg Thorington': {'EL': ['E', 'C'], 'CL': ['C', 'E'], 'Math': ['D', 'A'], 'Phy': ['F', 'B'], 'Chem': ['B', 'C']},
'Odis Levalley': {'EL': ['C', 'D'], 'CL': ['D', 'E'], 'Math': ['A', 'B'], 'Bio': ['C', 'B'], 'Chem': ['D', 'F']},
'Teodoro Negrin': {'EL': ['E', 'C'], 'CL': ['E', 'E'], 'Math': ['D', 'B'], 'Phy': ['B', 'A'], 'Bio': ['A', 'D']},
'Tobias Kimmer': {'EL': ['D', 'E'], 'CL': ['A', 'A'], 'Math': ['E', 'A'], 'Phy': ['E', 'B']},
'Maryam Brosius': {'EL': ['D', 'D'], 'CL': ['B', 'E'], 'Math': ['D', 'B'], 'Bio': ['F', 'B']},
'Darlena Crimi': {'EL': ['E', 'C'], 'CL': ['A', 'C'], 'Math': ['C', 'D'], 'Phy': ['C', 'B'], 'Bio': ['E', 'A'], 'Chem': ['C', 'C']},
'Marcella Daigneault': {'EL': ['E', 'B'], 'CL': ['C', 'B'], 'Math': ['E', 'B'], 'Phy': ['B', 'E'], 'Bio': ['C', 'C']},
'Dannette Raasch': {'EL': ['C', 'C'], 'CL': ['A', 'C'], 'Math': ['B', 'D'], 'Phy': ['E', 'D'], 'Chem': ['E', 'B']},
'Farah Quon': {'EL': ['D', 'B'], 'CL': ['F', 'C'], 'Math': ['A', 'C'], 'Phy': ['F', 'B'], 'Bio': ['C', 'C'], 'Chem': ['F', 'A']},
'Apryl Soileau': {'EL': ['E', 'D'], 'CL': ['F', 'C'], 'Math': ['C', 'D'], 'Phy': ['B', 'E']},
'Reiko Stack': {'EL': ['D', 'B'], 'CL': ['D', 'E'], 'Math': ['A', 'C'], 'Phy': ['F', 'F']},
'Terrance Lauterbach': {'EL': ['C', 'E'], 'CL': ['A', 'C'], 'Math': ['C', 'C'], 'Chem': ['E', 'C']},
'Carola Tegeler': {'EL': ['C', 'E'], 'CL': ['E', 'B'], 'Math': ['B', 'E'], 'Bio': ['C', 'B'], 'Chem': ['C', 'B']}}

print("Task 1.1 - process data")
# Task 1.1
# The function process_data() returns a dictionary same as the
# return_dict above after reading the file "overall_grades.txt".
# You are to read "overall_grades.txt" line by line and construct
# this dictionary instead of just return solution_dict.
def process_data():
    records = []
    read_input_file("overall_grades.txt", records)
    records = list(map(lambda x: x.split(';')[:-1],records))

    results = {}
    for record in records:
        results[record[0]] = {}
        for ele in record[1:]:
            subj, grades = ele.split(':')
            grade1, grade2 = grades.split(',')
            results[record[0]][subj] = [grade1, grade2]
    return results

print("Pass!" if process_data() == solution_dict else "Fail!")

print("\nTask 1.2 - exact n improved")
# Task 1.2
# The function returns the names of students
# who shows exactly n subjects improvement.
# You are to use the data in "overall_grades.txt".
def have_n_improvement(n):
    results = []
    dict1 = process_data()
    for name in dict1.keys():
        count = 0
        for subj in dict1[name]:
            grade1, grade2 = dict1[name][subj]
            if grade1 > grade2:
                count += 1
        if count == n:
            results.append(name)
    return results

for i in [0,1,2,3,4,5,6]:
    print(have_n_improvement(i))
    print(len(have_n_improvement(i)))

print("\nTask 1.3 - all improved")
# Task 1.3
# The function returns the names of students
# who shows improvement in all his/her subjects.
# You are to use the data in "overall_grades.txt".
def have_improvement_in_all_subjs():
    results = []
    dict1 = process_data()
    for name in dict1.keys():
        improve = True
        for subj in dict1[name]:
            grade1, grade2 = dict1[name][subj]
            if grade1 <= grade2:
                improve = False
        if improve:
            results.append(name)
    return results

print(have_improvement_in_all_subjs())

print("\nTask 1.4 - Combi")
# Task 1.4
# This function returns the total number of students who
# take all the subjects as indicated by the list combi
# Students who take more subjects than what is indicated
# in combi are also included.
# You are to use the data in "overall_grades.txt".
def count_combi(combi):
    dict1 = process_data()
    count = 0
    for name in dict1.keys():
        if set(combi).issubset(set(dict1[name].keys())):
            count += 1
    return count

print(count_combi(["EL"]))
print(count_combi(["Math"]))
print(count_combi(["CL"]))
print(count_combi(["EL", "Math"]))
print(count_combi(["EL", "Math", "CL"]))
print(count_combi(["EL", "Math", "CL", "Phy", "Chem", "Bio"]))
print(count_combi(["Phy"]))
print(count_combi(["Chem"]))
print(count_combi(["Bio"]))
print(count_combi(["Phy", "Chem"]))
print(count_combi(["Phy", "Bio"]))
print(count_combi(["Chem", "Bio"]))
print(count_combi(["Phy", "Chem", "Bio"]))

# Task 1.5
# Using the solution in Task 1.4
# Find the total number of students
# who take "Chem" and "Bio" but not "Physics"
# You are to use the data in "overall_grades.txt".
print("\nTask 1.5 - Chem Bio Only")
print(count_combi(["Chem", "Bio"]) - count_combi(["Phy", "Chem", "Bio"]))

print("\nTask 1.6 - GPA")
# Task 1.6
# This function calculates the GPA of a student according to their grades.
# The points for each grade is as {'A':5, 'B':4, 'C':3, 'D':2, 'E':1, 'F':0}
# The 1st and 2nd sem grades in the data has the same weightages.
# To calculate GPA,
# 1) Find the average points acheived of each subject.
#    e.g. if a student gets C and D in "CL", his average points for "CL" is 3 + 2 = 2.5
# 2) add up the average points of each subject and
#    then divide the total by the number subjects the student takes
#    e.g. 'Claudette Bode': {'EL': ['C', 'D'], 'CL': ['D', 'A'], 'Math': ['A', 'D'], 'Phy': ['A', 'D'], 'Bio': ['D', 'C']},
#    [(3 + 2)/2 + (2 + 5)/2 + (5 + 2)/2 + (2 + 5)/2 + (2 + 3)/2]/5 = 3.1
#    GPA for 'Claudette Bode' = 3.1
# You are to use the data in "overall_grades.txt".
def calculate_GPA(name):
    dict1 = process_data()
    map_points = {'A':5, 'B':4, 'C':3, 'D':2, 'E':1, 'F':0}
    total = 0
    for sub in dict1[name]:
        grade1, grade2 = dict1[name][sub]
        total += (map_points[grade1] + map_points[grade2])/2
    return total/len(dict1[name].keys())


print('Claudette Bode', calculate_GPA('Claudette Bode')) #3.1

print("\nTask 1.7 - Top 3")
# Task 1.7
# This function returns a list that contains 3 student's name
# who has the 3 highest GPA points.
# You are to use the data in "overall_grades.txt".
def top_3():
    def calculate_GPA(dict1, name):
        map_points = {'A':5, 'B':4, 'C':3, 'D':2, 'E':1, 'F':0}
        total = 0
        for sub in dict1[name]:
            grade1, grade2 = dict1[name][sub]
            total += (map_points[grade1] + map_points[grade2])/2
        return total/len(dict1[name].keys())
    dict1 = process_data()
    results = []
    for name in dict1.keys():
        gpa = calculate_GPA(dict1, name)
        if len(results) < 3:
            results.append(name)
        else:
            gpa1 = calculate_GPA(dict1, results[0])
            gpa2 = calculate_GPA(dict1, results[1])
            gpa3 = calculate_GPA(dict1, results[2])
            lowest = min(gpa, gpa1, gpa2, gpa3)
            if lowest == gpa1:
                results[0]= name
            elif lowest == gpa2:
                results[1]= name
            elif lowest == gpa3:
                results[2]= name
            else:
                pass
    return results

print(top_3())
##dict1 = process_data()
##for name in dict1.keys():
##    print("{:<30} {:<5}".format(name, calculate_GPA(name)))
##1 Tashia Bowen                   4.0
##2 Toney Mcnab                    3.625
##3 Carolann Kintner               3.5  
##4 Russell Gillison               3.375
