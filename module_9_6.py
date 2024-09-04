def all_variants(txt):
    length = len(txt)
    for i in range(length, 0, -1):
        for j in range(0, i):
            yield txt[j:j + length + 1 - i]

a = all_variants('abc')

for i in a:
    print(i)
