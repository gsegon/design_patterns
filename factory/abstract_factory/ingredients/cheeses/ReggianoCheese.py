from factory.abstract_factory.ingredients.cheeses.Cheese import Cheese


class ReggianoCheese(Cheese):
    """ Implements Cheese """

    def __init__(self):
        print('Reggiano cheese.')
