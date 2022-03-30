from iterator.menus.MenuItem import MenuItem
from iterator.iterators.DinerMenuIterator import DinerMenuIterator
from iterator.iterators.CafeMenuIterator import CafeMenuIterator

class CafeMenu:
    """ Implements a Diner Menu - A menu using 'numpy.ndarray' as a MenuItem collection """

    def __init__(self):
        """ Initialize the MenuItem collection """

        self.menu_items = {}

        self.add_item("Veggie Burger and Air Fries",
                      "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
                      True,
                      3.99)

        self.add_item("Soup of the day",
                      "A cup of the soup of the day, with a side salad",
                      False,
                      3.69)

        self.add_item("Burrito",
                      "A large burrito, with whole pinto beans, salsa, guacamole ",
                      True,
                      4.29)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float):
        """ Add item to the collection """
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items[name] = menu_item

    def create_iterator(self) -> DinerMenuIterator:
        """ Create a DinerMenu Iterator """
        return CafeMenuIterator(self.menu_items)
