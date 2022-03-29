import numpy as np
from iterator.MenuItem import MenuItem


class DinerMenu:

    def __init__(self):
        self.MAX_ITEMS = 6
        self.num_of_items = 0
        self.menu_items = np.empty(shape=(self.MAX_ITEMS,), dtype=MenuItem)

        self.add_item("Vegetarian BLT",
                      "(Fakin') Bacon with lettuce & tomato on whole wheat",
                      True,
                      2.99)

        self.add_item("BLT",
                      "Bacon with lettuce & tomato on whole wheat",
                      True,
                      2.99)

        self.add_item("Soup of the day",
                      "Soup of the day, with a side of potato salad",
                      False,
                      3.29)

        self.add_item("Hotdog",
                      "A hot dog, with sauerkraut, relish, onions, topped with cheese",
                      False,
                      3.05)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float):
        menu_item = MenuItem(name, description, vegetarian, price)
        if self.num_of_items >= self.MAX_ITEMS:
            raise Exception("Sorry, menu is full! Can't add item to menu")
        else:
            self.menu_items[self.num_of_items] = menu_item
            self.num_of_items += 1

    def get_menu_items(self) -> np.ndarray:
        return self.menu_items

