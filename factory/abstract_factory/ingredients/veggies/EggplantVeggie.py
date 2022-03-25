from factory.abstract_factory.ingredients.veggies.Veggie import Veggie


class EggplantVeggie(Veggie):
    """ Implements Veggie """

    def __init__(self):
        print('Eggplant.')
