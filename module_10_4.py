from threading import Thread, active_count
from time import sleep
from random import randint
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.tables = args
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for i in guests:
            k = 0
            for j in tables:
                if j.guest == None:
                    j.guest = i
                    i.start()
                    print(f'{i.name} сел(-а) за стол номер {j.number}')
                    break
                else:
                    k += 1
            if k == len(tables):
                self.queue.put(i)
                print(f'{i.name} в очереди')

    def discuss_guests(self):
        while True:
            for i in tables:
                if (not i.guest is None):
                    if not i.guest.is_alive():
                        print(f'{i.guest.name} покушал(-а) и ушёл(ушла)')
                        i.guest = None
                        print(f'cтол номер {i.number} свободен.')
                        if self.queue.empty() == False:
                            i.guest = self.queue.get()
                            print(f'{i.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i.number}')
                            i.guest.start()
            if active_count() == 1:
                break

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)

cafe.guest_arrival(*guests)
cafe.discuss_guests()
