import abc
import abc
from abc import *


class shape(ABC):
    def __init__(self, dimensions):
        self.dimensions = dimensions

    @abstractmethod
    def area(self):
        pass


class rectangle(shape):
    def __init__(self, dimensions):
        super().__init__(dimensions)

    def area(self, length, breadth):
        return length * breadth


class triangle(shape):
    def __init__(self, dimensions):
        super().__init__(dimensions)

    def area(self, base, height):
        return base * height * 0.5


class square(shape):
    def __init__(self, dimensions):
        super().__init__(dimensions)

    def area(self, length):
        return length * length


r = rectangle(4)
t = triangle(3)
s = square(4)
print(f"Rectangle area = {r.area(5, 9)}\nTriangle area = {t.area(3, 5)}\nSquare area = {s.area(3)}")