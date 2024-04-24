toppings = []


while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping == 'quit':
        break
    
    toppings.append(topping)
    print("Adding", topping, "to your pizza.\n")

total_price = 10 + (2.5 * len(toppings))


print("\nYour pizza with the following toppings:")
for topping in toppings:
    print("-", topping)
print("\nTotal price:", total_price)
