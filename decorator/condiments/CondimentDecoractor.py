from abc import abstractmethod
from decorator.beverages.Beverage import Beverage


class CondimentDecorator(Beverage):
    """ Defines an interface for the Condiment Decorator """

    def __init__(self, beverage):
        """ Defines the init """
        self.beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        """ Defines the description getter """
        return ''

    def get_size(self) -> str:
        """ Returns size of the beverage """
        return self.beverage.get_size()
    