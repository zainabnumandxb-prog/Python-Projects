import math

import math

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        diagonal = (self.width ** 2) + (self.height ** 2)
        return math.sqrt(diagonal)

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ('*' * self.width + '\n') * self.height
        return picture

    def get_amount_inside(self, other_shape) -> int:
        fit_width = self.width // other_shape.width
        fit_height = self.height // other_shape.height
        return fit_width * fit_height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def set_side(self, side: int):
        self.width = side
        self.height = side

    def set_width(self, width: int):
        self.set_side(width)

    def set_height(self, height: int):
        self.set_side(height) 
    
    def __str__(self):
        return f'Square(side={self.width})'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))