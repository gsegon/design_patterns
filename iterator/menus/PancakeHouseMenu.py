from iterator.menus.MenuItem import MenuItem
from iterator.iterators.PancakeHouseMenuIterator import PancakeHouseMenuIterator


class PancakeHouseMenu:
    """ Implements a PancakeHouse Menu - A menu using 'list' as a MenuItem collection """

    def __init__(self):
        """ Initialize the MenuItem collection """
        self.menu_items = []
        self.add_item("K&B\'s Pancake Breakfast",
                      "Pancakes with scrambled eggs and toast",
                      True,
                      2.99)

        self.add_item("Regular Pancake Breakfast",
                      "Pancakes with fried eggs, sausage",
                      False,
                      2.99)

        self.add_item("Blueberry Pancakes",
                      "Pancakes made with fresh Blueberries",
                      True,
                      3.49)

        self.add_item("Waffles",
                      "Waffles with your choice of blueberries or strawberries",
                      True,
                      3.59)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float):
        """ Add item to the collection """
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(menu_item)

    def create_iterator(self) -> PancakeHouseMenuIterator:
        """ Create a DinerMenu Iterator """
        return PancakeHouseMenuIterator(self.menu_items)
