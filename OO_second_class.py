


class Square:
    def __init__(self, a, x, y):
        self.a = a
        self.__x = x
        self.__y = y

    def area(self):
        return self.a ** 2


if __name__ == "__main__":
    my_square = Square(7, 0, 0)
    print(type(my_square))
    print(my_square)

    print(dir(my_square))
    print(my_square._Square__x)
    print(my_square.area())

