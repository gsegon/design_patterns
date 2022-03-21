from factory.abstract_factory.ingredients.veggies.Veggie import Veggie


class RedPepperVeggie(Veggie):

    def __init__(self):
        print('Red pepper.')
