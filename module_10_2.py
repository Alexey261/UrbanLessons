from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        self.power = power
        super().__init__(name=name)

    def run(self):
        enemies = 100
        days = 0
        print(f'{self.name}! На нас напали!')
        while True:
            if enemies <= 0:
                break
            days += 1
            enemies -= self.power
            print(f'{self.name} сражается {days} {"день" if days == 1 else "дня" if days in (2,3,4) else "дней"}, осталось {enemies} врагов')
            sleep(0.5)
        print(f'{self.name} одержал победу спустя {days} дней')


first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')