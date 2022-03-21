from factory.abstract_factory.ingredients.pepperoni.Pepperoni import Pepperoni


class SlicedPepperoni(Pepperoni):

    def __init__(self):
        print('Sliced pepperoni.')
