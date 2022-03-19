from abc import abstractmethod
from decorator.beverages.Beverage import Beverage


class CondimentDecorator(Beverage):

    def __init__(self, beverage):
        self.beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        return ''

    def get_size(self) -> str:
        return self.beverage.get_size()
    