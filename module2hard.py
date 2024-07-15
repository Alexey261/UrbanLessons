def inp_num():
    while True:
        numb = input(f'Введите случайное число от 3 до 20: ')
        if len(numb) == 0:
            print("  Вы ничего не ввели! ")
        elif numb.isnumeric() == False:
            print("  Вы ввели не число! ")
        elif int(numb) < 3 or int(numb) > 20:
            print("  Ваше число вне указанного диапазона! ")
        else:
            break
    return (int(numb))


rock_num = inp_num()
pass_str = ''
for i in range(1, rock_num):
    for j in range(i + 1, rock_num):
        if rock_num % (i + j) == 0:
            pass_str += (str(i) + str(j))
print(f'Ваш пароль: {pass_str}')
