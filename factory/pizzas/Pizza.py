from abc import ABC


class Pizza(ABC):

    def __init__(self):
        self.name = ''
        self.dough = ''
        self.sauce = ''
        self.toppings = []

    def prepare(self):
        print('Preparing ', self.name)
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings: ', [topping for topping in self.toppings])

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def get_name(self):
        return self.name