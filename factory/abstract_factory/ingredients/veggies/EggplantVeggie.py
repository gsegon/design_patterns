from factory.abstract_factory.ingredients.veggies.Veggie import Veggie


class EggplantVeggie(Veggie):

    def __init__(self):
        print('Eggplant.')
