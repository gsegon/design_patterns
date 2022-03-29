from iterator.iterators.Iterator import Iterator
from iterator.menus.MenuItem import MenuItem

import numpy as np


class DinerMenuIterator(Iterator):
    """ Diner menu Iterator - Implements Iterator """

    def __init__(self, items: np.ndarray):
        """ Initialize with the collection to iterate - items """
        self.items = items
        self.position = 0

    def next(self) -> MenuItem:
        """ return the next item from the collection """
        menu_item = self.items[self.position]
        self.position = self.position + 1
        return menu_item

    def has_next(self) -> bool:
        """ Check if the collection has a next item """
        if (self.position >= self.items.size) or self.items[self.position] is None:
            return False
        else:
            return True
