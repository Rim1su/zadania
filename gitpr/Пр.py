class Products:

    on_shelf = 0
    name = ""

    def __init__(self, name):
        self.name = name
        Products.on_shelf += 1
        print(name)
    def display_count(self):
        print('Всего продуктов: %d' % Products.on_shelf)

products = Products("Сыр")
products2 = Products("Хлеб")
products3 = Products("Масло")
products4 = Products("Яйца")
products5 = Products("Кетчуп")
products6 = Products("Соль")
products.display_count()
