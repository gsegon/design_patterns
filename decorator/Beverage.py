from abc import ABC, abstractmethod


class Beverage(ABC):

    def __init__(self):
        self.description = 'Unknown Beverage'

        self.sizes = ['TALL', 'GRANDE', 'VENTI']
        self.size = 'TALL'

    @abstractmethod
    def cost(self) -> float:
        return 0.0

    def get_description(self) -> str:
        return self.description

    def set_size(self, size: str):
        self.size = size

    def get_size(self) -> str:
        return self.size
