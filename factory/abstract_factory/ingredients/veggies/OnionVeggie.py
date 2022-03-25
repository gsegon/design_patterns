from factory.abstract_factory.ingredients.veggies.Veggie import Veggie


class OnionVeggie(Veggie):
    """ Implements Veggie """

    def __init__(self):
        print('Onion.')
