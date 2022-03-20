from abc import ABC


class Pizza(ABC):

    def prepare(self):
        print('Preparing ', self.__class__.__name__, '...')

    def bake(self):
        print('Baking ', self.__class__.__name__, '...')

    def cut(self):
        print('Cutting ', self.__class__.__name__, '...')

    def box(self):
        print('Boxing ', self.__class__.__name__, '...')