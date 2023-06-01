#Создание базового класса "Фигура" и его наследование для создания классов "Квадрат", "Прямоугольник" и "Круг". Класс "Фигура"
# будет иметь общие методы, такие как вычисление площади и периметра, а классы наследники будут иметь свои уникальные свойства и методы

import math

class Figure:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

s = Square(5)
print(s.area())  # выведет 25
print(s.perimeter())  # выведет 20

r = Rectangle(4, 5)
print(r.area())  # выведет 20
print(r.perimeter())  # выведет 18

c = Circle(3)
print(c.area())  # выведет приблизительно 28.27
print(c.perimeter())  # выведет приблизительно 18.85