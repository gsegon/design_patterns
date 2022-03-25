from factory.abstract_factory.ingredients.clams.Clams import Clams


class FreshClams(Clams):
    """ Implements Clams """

    def __init__(self):
        print('Fresh clams.')
