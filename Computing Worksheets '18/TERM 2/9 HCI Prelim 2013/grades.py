

def HighestAndAverage():
      f = open('MARKS.txt')
      grades = []
      for line in f:
            line = line.strip().split(',')
            # id , name , marks
            grades.append(line)
      f.close()

      average = 0
      highest = int(grades[0][2])
      for student in range(len(grades)):
            mark = int(grades[student][2])
            average += mark
            if mark > highest:
                  highest = mark
      tops = []
      for student in range(len(grades)):
            mark = int(grades[student][2])
            if highest == mark:
                  tops.append(grades[student][1])
      average = round(average / len(grades),2)

      print("Highest Mark: " + str(highest))
      print("Students: " + ', '.join(tops))
      print("Average Mark of module: " + str(average))
            
      return [highest,average]
      
def AssignGrade(mark,module_performance):
      mark = float(mark)
      highest = float(module_performance[0])
      average = float(module_performance[1])
      if mark == highest:
            return 'M'
      elif mark < average - 10:
            return 'F'
      else:
            return 'P'

def GradingSystem():
      f = open('MARKS.txt')
      grades = []
      for line in f:
            line = line.strip().split(',')
            # id , name , marks
            grades.append(line)
      f.close()

      module_performance = HighestAndAverage()
      
      for student in range(len(grades)):
            student = grades[student]
            student.append(module_performance[1])
            student.append(AssignGrade(student[2],module_performance))

      g = open('GRADES.txt','w')
      for student in range(len(grades)):
            student = grades[student]
            for i in range(len(student)):
                  student[i] = str(student[i])
            student = ','.join(student)
            student += '\n'
            g.write(student)
      g.close()
      
      





















      
