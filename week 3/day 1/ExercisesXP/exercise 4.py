class Zoo : 
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self,new_animal):
        if new_animal not in self.animals : 
            self.animals.append(new_animal)

    def get_animal(self):
        print(self.animals)

    def sell_animals(self,animal_sold) :
        if animal_sold in self.animals :
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted(self.animals)
        
        sorted_animal = sorted(self.animals)
        
        animal_group = {}
        for animal in sorted_animal:
            first_letter = animal[0]

            if first_letter in animal_group : 
                animal_group[first_letter].append(animal)
            else :
                animal_group[first_letter] = [animal]
        return animal_group
    
    def get_groups(self):
        animal_group = self.sort_animals()

        for group,animals in animal_group.items():
            print(f"Group: {group}")
            for animal in animals:
                print(animal)
            print()

ramat_gan_safari = Zoo("Ramat Gan Safari")

while True :
    animal = input("Which animal should we add to the zoo (or 'exit' to stop)")
    if animal.lower() == "exit":
        break
    ramat_gan_safari.add_animal(animal)

ramat_gan_safari.get_animal()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()






