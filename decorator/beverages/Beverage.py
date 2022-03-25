from abc import ABC, abstractmethod


class Beverage(ABC):

    def __init__(self):
        """ Initialize the beverage. """
        self.description = 'Unknown Beverage'

        self.sizes = ['TALL', 'GRANDE', 'VENTI']
        self.size = 'TALL'

    @abstractmethod
    def cost(self) -> float:
        """ Return the cost """
        return 0.0

    def get_description(self) -> str:
        """ Get description """
        return self.description

    def set_size(self, size: str):
        """ Set size """
        self.size = size

    def get_size(self) -> str:
        """ Get size """
        return self.size
