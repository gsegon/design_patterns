from factory.abstract_factory.ingredients.veggies.Veggie import Veggie


class SpinachVeggie(Veggie):
    """ Implements Veggie """

    def __init__(self):
        print('Spinach.')
