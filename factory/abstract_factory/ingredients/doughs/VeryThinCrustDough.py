from factory.abstract_factory.ingredients.doughs.Dough import Dough


class VeryThinCrustDough(Dough):
    """ Implements Dough """

    def __init__(self):
        print('Very thin crust dough')
