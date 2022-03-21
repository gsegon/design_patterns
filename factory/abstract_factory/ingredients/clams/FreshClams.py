from factory.abstract_factory.ingredients.clams.Clams import Clams


class FreshClams(Clams):

    def __init__(self):
        print('Fresh clams.')
