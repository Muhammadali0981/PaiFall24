

class student():
    def __init__(self, name:str, id: str):
        self.name = name
        self.id = id

    def print_details(self):
        print(f'name : {self.name}\nid : {self.id}')


class marks(student):
    def __init__(self, name:str, id: str, algo: float, ds: float,cal: float):
        super().__init__(name, id)
        self.marks_algo = algo
        self.marks_dataScience = ds
        self.marks_calculus = cal


    def print_marks(self):
        print(f'Algo marks : {self.marks_algo}\nDS marks : {self.marks_dataScience}\nCalculus marks : {self.marks_calculus}')

class result(marks):
    def __init__(self,name:str, id: str, algo: float, ds: float,cal: float, total: float, avg: float):
        super().__init__(name, id, algo, ds, cal)
        self.avg = avg
        self.total = total

    def calculate(self):
        self.total = 0
        self.total += self.marks_algo
        self.total += self.marks_calculus
        self.total += self.marks_dataScience
        self.avg = self.total/3
        print(self.total, self.avg)

r = result('ali','23k0052',34,60,90,0,0)
r.print_details()
r.print_marks()
r.calculate()

