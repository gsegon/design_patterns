from decorator.beverages.Beverage import Beverage


class DarkRoast(Beverage):
    """ Implements Dark Roast Beverage """

    def __init__(self):
        """ Initialize the Dark Roast """
        super(DarkRoast, self).__init__()
        self.description = 'Dart Roast coffee'

    def cost(self) -> float:
        """ Get cost """
        return 0.99
