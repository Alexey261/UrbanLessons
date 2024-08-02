def test_function():
    def inner_function():
        message = 'Я в области видимости функции test_function'
        print(message)
    inner_function()


test_function()

try:
    inner_function()
except NameError:
    if not('inner_function' in vars().keys()):
        print('Функция inner_function является вложенной и недоступна вне функции test_function!')
    else:
        print('В программе возникла ошибка! Выполнение прервано!')


