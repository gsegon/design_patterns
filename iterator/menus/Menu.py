from abc import ABC, abstractmethod
from iterator.iterators.Iterator import Iterator


class Menu(ABC):

    @abstractmethod
    def create_iterator(self) -> iter:
        pass
