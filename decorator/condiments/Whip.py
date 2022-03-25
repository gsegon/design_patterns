from decorator.condiments.CondimentDecoractor import CondimentDecorator


class Whip(CondimentDecorator):
    """ Implements the Whip decorator """

    def get_description(self) -> str:
        """ Appends the specific condiment description """
        return self.beverage.get_description() + ', Whip'

    def cost(self) -> float:
        """ Adds the specific condiment cost """
        return self.beverage.cost() + 0.10
