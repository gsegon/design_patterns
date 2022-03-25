from decorator.beverages.Beverage import Beverage


class HouseBlend(Beverage):
    """ Implements House Blend Beverage """

    def __init__(self):
        """ Initialize """
        super(HouseBlend, self).__init__()
        self.description = 'House Blend Coffe'

    def cost(self) -> float:
        """ Get cost """
        return 0.89
