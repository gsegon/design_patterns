from iterator.MenuItem import MenuItem


class PancakeHouseMenu:

    def __init__(self):
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
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(menu_item)

    def get_menu_items(self) -> list:
        return self.menu_items
