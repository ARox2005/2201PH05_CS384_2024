def addnames(students, name, grades):
  name = name.lower()
  students[name] = grades

def updateGrades(students, name, grades):
  name = name.lower()
  if name in students:
    students[name] = grades
  else:
    print(f"Student {name} does not exist")

# def printAvg(students):
#   for name, grades in students.items():
#     avg = sum(grades) / len(grades)
#     print(f"{name.capitalize()} - Average : {avg}")

def sorting(students):
  avgs = []
  for name, grades in students.items():
    avg = sum(grades) / len(grades)
    avgs.append((name, avg))
  n = len(avgs)
  for i in range(n):
    for j in range(0, n-i-1):
      if avgs[j][1] < avgs[j+1][1]:
        avgs[j], avgs[j+1] = avgs[j+1], avgs[j]

  for name, avg in avgs:
    print(f"{name.capitalize()} - Average : {avg:.2f}")

students = {}

n=int(input("Enter number of students : "))
for i in range(n):
  names = input("Enter name of student : ")
  grades = []
  for j in range(3):
    grade = int(input(f"Enter grade {j+1} : "))
    grades.append(grade)
  addnames(students, names, grades)

sorting(students)

u = int(input("To update grades of a student Press 1\nTo add another student Press 2 : "))

if u == 1:
  name = input("Enter name of student : ")
  grades = []
  for j in range(3):
    grade = int(input(f"Enter grade {j+1} : "))
    grades.append(grade)
elif u == 2:
  updateGrades(students, name, grades)

sorting(students)
