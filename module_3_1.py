calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(testr):
    count_calls()
    return (len(testr), testr.upper(), testr.lower())


def is_contains(string, list_to_search):
    str_flag = False
    for i in list_to_search:
        if i.casefold() == string.casefold():
            str_flag = True
            break
    count_calls()
    return str_flag

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
