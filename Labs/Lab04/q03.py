class student:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def print_biodata(self):
        print(f'name = {self.name}\nage = {self.age} ')

s1 = student('ali', 19)
s1.print_biodata()