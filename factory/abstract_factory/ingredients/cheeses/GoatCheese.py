from factory.abstract_factory.ingredients.cheeses.Cheese import Cheese


class GoatCheese(Cheese):
    """ Implements Cheese """

    def __init__(self):
        print('Goat cheese.')
