class Figure():
    sides_count = 0

    def __init__(self, color, *args):

        if len([*args]) == self.sides_count:
            self.__sides = [*args]
        else:
            self.__sides = [1] * self.sides_count

        self.__color = list(color)

        if not self.__is_valid_color(self.__color):
            self.__color = [255, 255, 255]

        self.filled = True

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_color(self, rgb):
        return all(_ <= 255 and _ >= 0 for _ in rgb)

    def __is_valid_sides(self, *args):
        return len([*args]) == self.sides_count and all(isinstance(_, int) for _ in [*args])

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color([r, g, b]):
            self.__color = [r, g, b]

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

    def get_sides(self):
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args):
        if len([*args]) == 1 and isinstance(args[0], int) and args[0] > 0:
            self.__radius = args[0] / (3.1415926535 * 2)
        else:
            self.__radius = 0
        super().__init__(color, *args)

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *args):
        if len([*args]) == 3 and all(isinstance(_, int) for _ in [*args]) and all(_ > 0 for _ in [*args]):
            a, b, c = [*args]
            if not (a + b > c and a + c > b and b + c > a):
                [*args] = [1] * 3
        super().__init__(color, *args)

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** (0.5)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *args):

        if len([*args]) == 1 and isinstance(args[0], int) and args[0] > 0:
            cube_sides = args * 12
        else:
            cube_sides = [1] * 12

        super().__init__(color, *cube_sides)

    def set_sides(self, *new_sides):
        if [*new_sides].count(new_sides[0]) == len([*new_sides]):
            super().set_sides(*new_sides)

    def get_volume(self):
        return self.get_sides()[0]**3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())