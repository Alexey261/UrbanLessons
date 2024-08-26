def custom_write(nm, lst):
    strings_positions = {}
    with open(nm, 'w', encoding='utf-8') as file:
        for _ in lst:
            i = lst.index(_) + 1
            j = file.tell()
            strings_positions[(i, j)] = _
            file.write(_ + '\n')

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
