from factory.abstract_factory.ingredients.doughs.Dough import Dough


class VeryThinCrustDough(Dough):

    def __init__(self):
        print('Very thin crust dough')
