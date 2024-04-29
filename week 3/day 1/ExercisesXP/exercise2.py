class Dog():
    def __init__(self,name,height):
        self.name = name 
        self.height = height 

    def bark(self):
        print(f"{self.name} goes woof")

    def jump(self):
        x = self.height * 2 
        print(f"{self.name} jumps {x} cm high!")

davids_dog = Dog("Rex", 50)
print(f"David's dog is called {davids_dog.name} and his height is {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"David's dog is called {sarahs_dog.name} and his height is {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger.")

