#teenagers
teenagers = ["Alicia", "Zarah", "Thomas", "David", "Eva"]

for teenager in teenagers[:]:  
    age = int(input(f"Age of {teenager}: "))
    if not 16 <= age <= 21:
        teenagers.remove(teenager)

print("Teenagers permitted to watch the movie:", teenagers)