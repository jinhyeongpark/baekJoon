students = list(range(1, 31))

for i in range(28):
    student = int(input())
    students.remove(student)

for num in students:
    print(num)
