from factory.abstract_factory.ingredients.veggies.Veggie import Veggie


class GarlicVeggie(Veggie):

    def __init__(self):
        print('Garlic.')
