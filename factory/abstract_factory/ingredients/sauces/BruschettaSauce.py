from factory.abstract_factory.ingredients.sauces.Sauce import Sauce


class BruschettaSauce(Sauce):

    def __init__(self):
        print('Bruschetta sauce.')
