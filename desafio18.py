import random

print("######### DESAFIO – 18 ##########")

students = []

for i in range(4):
    student = input("Name: ")
    students.append(student)

random.shuffle(students)
print(f"Student's names in random order: {students}")
