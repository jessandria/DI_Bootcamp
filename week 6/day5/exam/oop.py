class Vehicles :
    def __init__(self, type, brand, year):
        if not type or not brand or not isinstance(year, int):
            raise ValueError()
        self.type = type
        self.brand = brand
        self.year = year

    def display(self):
        print(self.type)
        print(self.brand)
        print(self.year)

Lambo = Vehicles("Lambo","Sport Car", 2003)
Lambo.display()

