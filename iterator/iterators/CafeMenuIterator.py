from iterator.iterators.Iterator import Iterator
from iterator.menus.MenuItem import MenuItem


class CafeMenuIterator(Iterator):
    """ Diner menu Iterator - Implements Iterator """

    def __init__(self, items: dict):
        """ Initialize with the collection to iterate - items """
        self.items = items
        self.list_values = list(self.items.values())
        self.position = 0

    def next(self) -> MenuItem:
        """ return the next item from the collection """
        menu_item = self.list_values[self.position]
        self.position = self.position + 1
        return menu_item

    def has_next(self) -> bool:
        """ Check if the collection has a next item """
        if self.position >= len(self.items):
            return False
        else:
            return True
