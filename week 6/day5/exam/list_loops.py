# Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers
list1 = []
for i in range(0,11):
    if i%2 == 0 :
        list1.append(i**2)

print(list1)

# Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3.
numbers = list(range(1, 11))
for n in numbers:
    if n%2 == 0 and n%3 == 0:
        print(n)

#Loop through the provided list of dictionaries and print the names and ages:
student_list = [
    {
    "name": "John", 
    "age": 24
    }, 
    {
    "name": "Anna", 
    "age": 22
    }, 
    {
    "name": "Mike", 
    "age": 25
    }
]

for student in student_list:
    name = student["name"]
    age = student["age"]
    print(f"Name: {name}, Age: {age}")

