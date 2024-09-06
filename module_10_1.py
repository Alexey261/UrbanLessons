from threading import Thread
from datetime import datetime
from time import sleep

import random


def simple_words_generator(n):
    vowels = 'аеиоуэюя'
    consonants = 'бвгджзклмнпрстфхцчшщ'
    c, s = '', ''
    for i in range(n):
        c = ''.join(random.choices(consonants, k=random.randint(1, 2)))
        if random.randint(0, 1):
            s += c + vowels[random.randint(0, 7)]
        else:
            s += vowels[random.randint(0, 7)] + c
    s = ''.join(sorted(set(s), key=s.index))
    return (s)


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Слово №{i + 1}:\t{simple_words_generator(3)}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
elapsed_time = time_end - time_start
print(f'Время работы функций: {elapsed_time}')

time_start = datetime.now()
first_thr = Thread(target=write_words, args=(10, 'example5.txt'))
second_thr = Thread(target=write_words, args=(30, 'example6.txt'))
third_thr = Thread(target=write_words, args=(200, 'example7.txt'))
fourth_thr = Thread(target=write_words, args=(100, 'example8.txt'))

first_thr.start()
second_thr.start()
third_thr.start()
fourth_thr.start()

first_thr.join()
second_thr.join()
third_thr.join()
fourth_thr.join()

time_end = datetime.now()
elapsed_time = time_end - time_start
print(f'Время работы потоков: {elapsed_time}')
