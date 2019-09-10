# Exercise 1
from random import randint
a = randint(1, 100)
b = randint(1, 100)

result = a + b

print("Exercise 1:")
print("Alice")
print(a)
print(b)
print("Sum = " + str(result))
print("Average = " + str(result / 2.0))


# Exercise 2
students = ["Jill", "Jacqueline", "Marcus"]
students.sort()

print("Exercise 2:")
print(students)

first_name = students[0]
first_name = first_name[:-1]
# [-1]: Gives the last character of the string
# [:-1]: Gives everything UP TO the last character
print(first_name)

longest_name = ''
for student in students:
    if len(student) > len(longest_name):
        longest_name = student
print(longest_name)



