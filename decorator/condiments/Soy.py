from decorator.condiments.CondimentDecoractor import CondimentDecorator


class Soy(CondimentDecorator):

    def get_description(self) -> str:
        return self.beverage.get_description() + ', Soy'

    def cost(self) -> float:

        if self.beverage.get_size() == self.beverage.sizes[0]:
            return self.beverage.cost() + 0.10
        elif self.beverage.get_size() == self.beverage.sizes[1]:
            return self.beverage.cost() + 0.15
        elif self.beverage.get_size() == self.beverage.sizes[2]:
            return self.beverage.cost() + 0.20
