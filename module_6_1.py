class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if (food.edible):
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Plant:

    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):

    def __new__(cls, *args, **kwargs):
        print(f'{args[0]}. Класс <{__class__.__name__}>. Родитель: <{__class__.__bases__[0].__name__}>')
        cls.instance = super().__new__(cls)
        return cls.instance

    def __str__(self):
        _child = __class__.__name__
        _parent = __class__.__bases__[0].__name__
        return f'Объект "{self.name}" класса <{_child}>, базовый класс: <{_parent}>. {"Живой." if self.alive else "Умер."}' \
               f' {"Сытый." if self.fed and self.alive else ("Голодный" if not self.fed and self.alive else "")}'

class Predator(Animal):

    def __new__(cls, *args, **kwargs):
        print(f'{args[0]}. Класс <{__class__.__name__}>. Родитель: <{__class__.__bases__[0].__name__}>')
        cls.instance = super().__new__(cls)
        return cls.instance

    def __str__(self):
        _child = __class__.__name__
        _parent = __class__.__bases__[0].__name__
        return f'Объект "{self.name}" класса <{_child}>, базовый класс: <{_parent}>. {"Живой." if self.alive else "Умер."}' \
               f' {"Сытый." if self.fed and self.alive else ("Голодный" if not self.fed and self.alive else "")}'


class Flower(Plant):

    def __new__(cls, *args, **kwargs):
        print(f'{cls._rainbow(cls, args[0])}. Класс <{__class__.__name__}>. Родитель: <{__class__.__bases__[0].__name__}>')
        cls.instance = super().__new__(cls)
        return cls.instance


    def __str__(self):
        _child = __class__.__name__
        _parent = __class__.__bases__[0].__name__
        return f'Объект "{self._rainbow(self.name)}" класса <{_child}>, базовый класс: <{_parent}>. {"съедобен" if self.edible else "Несъедобен."}'

    def _rainbow(self, s_t):
        colors = ["\033[31m{}", "\033[32m{}", "\033[33m{}", "\033[34m{}", "\033[35m{}", "\033[36m{}", "\033[37m{}"]
        _white = "\033[38m{}"
        _str = ''
        for i in range(len(s_t)):
            _str += f'{colors[i % 7].format(s_t[i])}'
        _str += f'{_white.format("")}'
        return _str


class Fruit(Plant):

    def __new__(cls, *args, **kwargs):
        print(f'{args[0]}. Класс <{__class__.__name__}>. Родитель: <{__class__.__bases__[0].__name__}>')
        cls.instance = super().__new__(cls)
        return cls.instance


    def __init__(self, name):
        self.name = name
        self.edible = True

    def __str__(self):
        _child = __class__.__name__
        _parent = __class__.__bases__[0].__name__
        return f'Объект "{self.name}" класса <{_child}>, базовый класс: <{_parent}>. {"Съедобен." if self.edible else "Несъедобен."}'


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print()

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)



