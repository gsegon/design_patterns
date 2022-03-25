from factory.abstract_factory.ingredients.doughs.Dough import Dough


class ThickCrustDough(Dough):
    """ Implements Dough """

    def __init__(self):
        print('Thick crust dough')
