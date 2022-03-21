from factory.abstract_factory.ingredients.sauces.Sauce import Sauce


class MarinaraSauce(Sauce):

    def __init__(self):
        print('Marinara sauce.')
