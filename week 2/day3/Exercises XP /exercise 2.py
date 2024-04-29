def ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    ticket_price = ticket_price(age)
    total_cost += ticket_price
    
print(f"Total cost for the family: ${total_cost}")





