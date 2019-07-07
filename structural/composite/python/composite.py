"""
Compose objects into tree structures to represent part-whole
hierarchies. Composite lets clients treat individual objects and
compositions of objects uniformly.
"""

import abc

class Menu(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def getValues(self):
        pass

class CompositeMenu(Menu):
    def __init__(self):
        self._childrens = set()

    def getValues(self):
        for child in self._childrens:
            child.getValues()

    def add(self, menu):
        self._childrens.add(menu)

    def remove(self, menu):
        self._childrens.discard(menu)

class Food(Menu):
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def getValues(self):
        output = 'Name: %s, price: %s' % (self.name, self.price)
        print(output)

class CompositePizza(Menu):
    def __init__(self):
        self._childrens = set()

    def getValues(self):
        for child in self._childrens:
            child.getValues()

    def add(self, menu):
        self._childrens.add(menu)

    def remove(self, menu):
        self._childrens.discard(menu)

def main():
    taco = Food(price=20, name='Taco')
    composite_pizza = composite_pizzas()

    composite_menu = CompositeMenu()
    composite_menu.add(taco)
    composite_menu.add(composite_pizza)

    composite_menu.getValues()

def composite_pizzas():
    pepperoni_pizza = Food(price=170, name='Pepperoni pizza')
    hawaiiana_pizza = Food(price=160, name='Hawaiiana pizza')

    composite_pizza = CompositePizza()
    composite_pizza.add(pepperoni_pizza)
    composite_pizza.add(hawaiiana_pizza)

    return composite_pizza

if __name__ == "__main__":
    main()
