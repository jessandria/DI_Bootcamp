#bonus
def ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15

family = {}


number = int(input("Number of family members: "))
for i in range(number):
    name = input("Family member's name: ")
    age = int(input("Family member's age: "))
    family[name] = age

total_cost = 0


for name, age in family.items():
    lastticket_price = ticket_price(age)
    total_cost += lastticket_price



print(f"Total cost for the family: ${total_cost}")
