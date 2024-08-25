class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return ', '.join(str(_) for _ in list(self.__dict__.values()))


class Shop:

    __file_name = 'products.txt'

    def prod_2_str(self, p):
        return ', '.join(str(_) for _ in list(p.__dict__.values()))

    def add(self, *products):

        for i in products:
            if not(self.prod_2_str(i) in self.get_products()):
                with open(self.__file_name, 'a') as file:
                    file.write(self.prod_2_str(i)+'\n')
            else:
                print(f'Продукт {self.prod_2_str(i)} уже есть в магазине!')

    def get_products(self):
        try:
            with open(self.__file_name) as file:
                _str = file.read()
        except IOError:
            _str = ''
        return _str

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())


