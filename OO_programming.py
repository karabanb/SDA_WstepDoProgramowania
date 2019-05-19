
import math

# możemy to zrobić tak

a = 4


def square_area(a):
    return a ** 2


def square_permiter(a):
    return 4 * a


print(square_area())


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


my_line = LineSegment((0, 0), (1, 1))

print(my_line.get_len())

