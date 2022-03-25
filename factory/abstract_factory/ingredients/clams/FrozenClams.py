from factory.abstract_factory.ingredients.clams.Clams import Clams


class FrozenClams(Clams):
    """ Implements Clams """

    def __init__(self):
        print('Frozen clams.')
