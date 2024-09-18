class Vehicle() :
    def __init__(self, cap) :
        self.cap = cap
        self.fare = self.cap*100

    def calculate(self) :
        self.fare = self.fare


class Bus(Vehicle) :
    def __init__(self,cap) :
        super().__init__(cap)

    def calculate(self) :
        self.fare = 1.10*self.fare


bus = Bus(100)
bus.calculate()
print(f"Bus has Seating capacity {bus.cap} and fare {bus.fare}")
