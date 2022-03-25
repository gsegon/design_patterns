from factory.abstract_factory.ingredients.cheeses.Cheese import Cheese


class MozzarellaCheese(Cheese):
    """ Implements Cheese """

    def __init__(self):
        print('Mozzarella cheese.')
