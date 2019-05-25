
import math

# możemy to zrobić tak

b = 4


def square_area(b):
    return b ** 2


def square_permiter(b):
    return 4 * b


print(square_area(b))


# podchodząc obiektowo zrobimy tak:

class Square:

    def __init__(self, a, x, y):
        self.a = a
        self.x = x
        self.y = y

    def area(self):
        return self.a ** 2


my_square = Square(7, 0, 0)
print(my_square.a)
print(my_square.x)
print(my_square.y)
print(my_square.area())


my_square2 = Square(2, 7, 7)
print(my_square2.area())


class LineSegment:

    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def get_len(self):
        return math.sqrt(
            ((self.point_1[0] - self.point_2[0]) ** 2
             + (self.point_1[1] - self.point_2[1]) ** 2)
        )

    def __str__(self):
        return f'LineSegment from({self.point_1},to {self.point_2})'

    def __repr__(self):
        return f'LineSegment({self.point_1}, {self.point_2})'

    def __eq__(self, other):
        if isinstance(other, LineSegment):
            return(self.point_1 == other.point_1
                   and self.point_2 == other.point_2)
        else:
            return False



my_line = LineSegment((0, 0), (1, 1))
my_second_line = LineSegment((0, 0), (1, 1))

print(id(my_line))
print(id(my_square))
print(my_line == my_second_line)

print(my_line == 7)

my_other_line = LineSegment((0, 0), (1, 2))
print(my_other_line == my_line)

print(my_line.get_len())
print(my_line)
print(repr(my_line))