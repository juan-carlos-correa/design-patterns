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

def main():
    taco = Food(price=20, name='Taco')
    pizza = Food(price=150, name='Pizza')

    composite_menu = CompositeMenu()
    composite_menu.add(taco)
    composite_menu.add(pizza)

    composite_menu.getValues()

if __name__ == "__main__":
    main()
