def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b = 25)
print_params(c = [1,2,3])

values_list = ["123", False, 10]
print_params(*values_list)

values_dict = {'a': True, 'c': 99.99, 'b': (0, 1, 2, 3)}
print_params(**values_dict)

values_list_2 = ['Some String', 123.456]
print_params(*values_list_2, 42)
