from factory.abstract_factory.ingredients.veggies.Veggie import Veggie


class GarlicVeggie(Veggie):
    """ Implements Veggie """

    def __init__(self):
        print('Garlic.')
