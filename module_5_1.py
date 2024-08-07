from time import sleep

class House:
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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)