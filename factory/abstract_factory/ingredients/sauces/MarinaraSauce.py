from factory.abstract_factory.ingredients.sauces.Sauce import Sauce


class MarinaraSauce(Sauce):
    """ Implements Sauce """

    def __init__(self):
        print('Marinara sauce.')
