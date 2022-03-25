from factory.abstract_factory.ingredients.veggies.Veggie import Veggie


class BlackOlivesVeggie(Veggie):
    """ Implements Veggie """

    def __init__(self):
        print('Black Olives.')
