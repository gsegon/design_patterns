from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Factories produce products and in our example the product is Pizza """

    def __init__(self):
        self.name = ''

        self.dough = None
        self.sauce = None
        self.veggies = None
        self.cheese = None
        self.pepperoni = None
        self.clams = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
