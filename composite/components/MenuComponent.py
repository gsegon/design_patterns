from abc import ABC, abstractmethod


class MenuComponent(ABC):
    """
    MenuComponent represents the interface for both MenuItem and Menu. (Node in a context of a Composite pattern)
    """

    def get_name(self) -> str:
        """ Returns the name """
        raise NotImplemented

    def get_description(self) -> str:
        """ Returns the description """
        raise NotImplemented

    def get_price(self) -> float:
        """ Returns the price """
        raise NotImplemented

    def is_vegetarian(self) -> bool:
        """ Returns True if vegetarian, otherwise false """
        raise NotImplemented

    def add(self, component: 'MenuComponent'):
        """ Add the component """
        raise NotImplemented

    def remove(self, component: 'MenuComponent'):
        """ Remove the component """
        raise NotImplemented

    def get_child(self, index: int) -> 'MenuComponent':
        """ Get child at the 'index' position """
        raise NotImplemented

    def __str__(self) -> str:
        raise NotImplemented
