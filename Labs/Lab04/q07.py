class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.fare = capacity * 100

    def print_fare(self):
        print(f"Fare is {self.fare}")


class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.fare = self.fare + self.fare*0.1


b1 = Bus(10)
b1.print_fare()