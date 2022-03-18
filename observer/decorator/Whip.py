from CondimentDecoractor import CondimentDecorator


class Whip(CondimentDecorator):

    def get_description(self) -> str:
        return self.beverage.get_description() + ', Whip'

    def cost(self) -> float:
        return self.beverage.cost() + 0.10
