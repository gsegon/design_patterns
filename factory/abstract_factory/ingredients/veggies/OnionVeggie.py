from factory.abstract_factory.ingredients.veggies.Veggie import Veggie


class OnionVeggie(Veggie):

    def __init__(self):
        print('Onion.')
