from abc import ABC, abstractmethod
from iterator.menus.MenuItem import MenuItem


class Iterator(ABC):

    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> MenuItem:
        pass
