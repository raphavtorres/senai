import random

print("######### DESAFIO – 16 ##########")

students = []
student = ''

for i in range(4):
    student = input("Name: ")
    students.append(student)

random.shuffle(students)
print(students[0])
