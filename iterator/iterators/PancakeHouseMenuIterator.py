from iterator.iterators.Iterator import Iterator
from iterator.menus.MenuItem import MenuItem


class PancakeHouseMenuIterator(Iterator):
    """ Diner menu Iterator - Implements Iterator """

    def __init__(self, items: list):
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
        if (self.position >= len(self.items)) or self.items[self.position] is None:
            return False
        else:
            return True
