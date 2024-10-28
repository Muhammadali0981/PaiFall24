class Animal:
    def __init__(self, n:str, age:int, h:str, a:bool):
        self.name = n
        self.age = age
        self.habitat = h
        self.available_for_viewing = a 

    def set_availability(self, a:bool):
        self.available_for_viewing = a

    def display_info(self):
        print(f'Name = {self.name}\nAge = {self.age}\nHabitat = {self.habitat}\nAvalibality = {self.available_for_viewing}')


class Bird(Animal):
    def __init__(self, n:str, age:int, h:str, a:bool, w:int, f:int):
        super().__init__(n, age, h, a)
        self.wingspan = w
        self.flight_altitude = f

    def display_info(self):
        super().display_info()
        print(f'Wingspan = {self.wingspan}\nFlight Altitude = {self.flight_altitude}')


class Mammal(Animal):
    def __init__(self, n:str, age:int, h:str, a:bool, f:int, d:str):
        super().__init__(n, age, h, a)
        self.diet_type = d
        self.fur_length = f

    def display_info(self):
        super().display_info()
        print(f'Diet Type = {self.diet_type}\nFur Length = {self.fur_length}')


class Reptile(Animal):
    def __init__(self, n:str, age:int, h:str, a:bool, s:str, v:bool):
        super().__init__(n, age, h, a)
        self.scale_pattern = s
        self.venomous_status = v

    def display_info(self):
        super().display_info()
        print(f'Scale Pattern = {self.scale_pattern}\nVenomous Status = {self.venomous_status}')


print("Bird Class:")
parrot = Bird(n="Mr.Parrot the parrot", age=2, h="Tropical Forest", a=True, w=30, f=100)
parrot.display_info()  
print("\n")

print("Mammal Class:")
lion = Mammal(n="Simba the lion", age=5, h="Savannah", a=False, f=5, d="Carnivore")
lion.display_info()  # Display info for lion
print("\n")

print("Reptile Class:")
cobra = Reptile(n="Cobra Kai the cobra", age=3, h="Desert", a=True, s="Smooth", v=True)
cobra.display_info() 
print("\n")


print("Setting Lion's availability to True (Available for viewing)...")
lion.set_availability(True)
lion.display_info()