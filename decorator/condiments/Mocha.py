from decorator.condiments.CondimentDecoractor import CondimentDecorator


class Mocha(CondimentDecorator):
    """ Implements the Mocha decorator """

    def get_description(self) -> str:
        """ Appends the specific condiment description """
        return self.beverage.get_description() + ', Mocha'

    def cost(self) -> float:
        """ Adds the specific condiment cost """
        return self.beverage.cost() + 0.20
