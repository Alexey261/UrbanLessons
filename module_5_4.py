from time import sleep


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(f'"{self.name}" снесён, но он останется в истории.')


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __elevator_progress_bar(self, n, m):
        for j in range(1, m + 1):
            board = '\u2502'
            for i in range(1, n + 1):
                if i == j:
                    board += str(i)
                else:
                    board += ' ' * len(str(i))
                board += '\u2502'

            print('\r' + board, end='', flush=True)
            sleep(1)
            board = ''

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor:
            print('\nТакого этажа не существует!')
        else:
            print(f'\nВас приветствует лифт "{self.name}"! \n\nОтправляемся на {new_floor}-й этаж.')
            self.__elevator_progress_bar(self.number_of_floors, new_floor)
            print(f'\nВы прибыли на {new_floor}-й этаж. Можно выходить.')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: "' + self.name + '". Количество этажей: ' + str(self.number_of_floors)

    def __eq__(self, other):
        if not isinstance(other, House):
            raise TypeError('Можно сравнивать только объекты типа "House"')
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, House):
            raise TypeError('Можно сравнивать только объекты типа "House"')
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            raise TypeError('Можно сравнивать только объекты типа "House"')
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, House):
            raise TypeError('Можно сравнивать только объекты типа "House"')
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, House):
            raise TypeError('Можно сравнивать только объекты типа "House"')
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
            raise TypeError('Можно сравнивать только объекты типа "House"')
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError('Для увеличения количества этажей требуется целое число!')
        self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        if not isinstance(value, int):
            raise TypeError('Тип прибавляемого числа должен быть int!')
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self + value


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
