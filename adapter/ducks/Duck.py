import abc
from abc import ABC, abstractmethod


class Duck(ABC):

    @abstractmethod
    def get_flying_capacity(self) -> float:
        return 0

    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass
    