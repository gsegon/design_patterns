from Beverage import Beverage


class DarkRoast(Beverage):

    def __init__(self):
        super(DarkRoast, self).__init__()
        self.description = 'Dart Roast coffee'

    def cost(self) -> float:
        return 0.99
