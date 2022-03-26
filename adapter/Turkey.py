from abc import ABC, abstractmethod


class Turkey(ABC):

    @abstractmethod
    def get_flying_capacity(self) -> float:
        return 0

    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass
