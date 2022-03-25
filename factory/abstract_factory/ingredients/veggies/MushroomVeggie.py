from factory.abstract_factory.ingredients.veggies.Veggie import Veggie


class MushroomVeggie(Veggie):
    """ Implements Veggie """

    def __init__(self):
        print('Mushroom.')

