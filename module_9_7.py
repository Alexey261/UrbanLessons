def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        a = []
        for i in range(1, num + 1):
            if (num / i).is_integer():
                a.append(i)
        if len(a) <= 2 :
            print('Простое')
        else:
            print('Составное')
        return num

    return wrapper


@is_prime
def sum_three(*args):  # or more than three...
    return sum([*args])


result = sum_three(2, 3, 6)
print(result)
