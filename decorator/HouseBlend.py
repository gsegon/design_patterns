from Beverage import Beverage


class HouseBlend(Beverage):

    def __init__(self):
        super(HouseBlend, self).__init__()
        self.description = 'House Blend Coffe'

    def cost(self) -> float:
        return 0.89
