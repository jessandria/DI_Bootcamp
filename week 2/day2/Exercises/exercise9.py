#family members
family_members = int(input("Enter the number of family members: "))
total_cost = 0



for member in range(family_members) : 
    age = int(input(f"Enter the age of family member {member + 1}: "))
    if age < 3 :
        ticket_price = 0 
    elif 3 <= age <= 12 :
        ticket_price = 10
    elif age > 12 :
        ticket_price = 15
    total_cost += ticket_price

print("Total cost:",total_cost)




