#Дополнительное практическое задание по модулю №1
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
avg_grades = {}

students = list(students)
students.sort()
for i in range (0,5):
    avg_grades.update ({ students[i] : sum(grades[i]) / len(grades[i] )})
print (avg_grades)