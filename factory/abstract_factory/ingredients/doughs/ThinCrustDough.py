from factory.abstract_factory.ingredients.doughs.Dough import Dough


class ThinCrustDough(Dough):
    """ Implements Dough """

    def __init__(self):
        print('Thin crust dough')
