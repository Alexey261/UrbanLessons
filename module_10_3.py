from threading import Thread, Lock
from time import sleep
from random import randint

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            debit = randint(50, 500)
            self.balance += debit
            print(f'Пополнение: {debit}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        for i in range(100):
            credit = randint(50, 500)
            print(f'Запрос на {credit}')
            if credit > self.balance:
                print('Запрос отклонён, недостаточно средств!')
                self.lock.acquire()
            else:
                self.balance -= credit
                print(f'Снятие: {credit}. Баланс: {self.balance}')
                sleep(0.001)



bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')