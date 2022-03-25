from decorator.beverages.Beverage import Beverage


class Espresso(Beverage):
    """ Implements Espresso Beverage """

    def __init__(self):
        """ Initialize """
        super(Espresso, self).__init__()
        self.description = 'Espresso'

    def cost(self) -> float:
        """ Get cost """
        return 1.99
