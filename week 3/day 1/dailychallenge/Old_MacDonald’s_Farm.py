class Farm():
    def __init__(self, Farm_name):
        self.name= Farm_name
        self.animals = {}
    
    def add_animal(self,animal,quantity=1): 
        if animal in self.animals: 
            self.animals[animal] += quantity
        else :
            self.animals[animal] = quantity

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, count in self.animals.items():
            info += f"\n{animal} : {count}\n" 

        info += "\n  E-I-E-I-0!"

        return info
    
    def get_animal_types (self): 
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_string = ", ".join(animal_types)
        if len(animal_types) > 1:
            animal_string += "s"
        return f"{self.name}'s farm has {animal_string}."
    


        
# Call code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())





