class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cookie = Cat("Cookie",3)
tigress = Cat("Tigress",7)
boullette = Cat("Boulette",5)

def find_oldest_cat(cats):
    oldest_cat = None
    max_age = 0

    for cat in cats:
        if cat.age > max_age:
            max_age = cat.age
            oldest_cat = cat
    
    return oldest_cat

cats = [cookie, tigress, boullette]

oldest_cat = find_oldest_cat(cats)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old")




        




