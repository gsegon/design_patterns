from Beverage import Beverage


class Espresso(Beverage):

    def __init__(self):
        super(Espresso, self).__init__()
        self.description = 'Espresso'

    def cost(self) -> float:
        return 1.99
