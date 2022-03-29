from iterator.menus.DinerMenu import DinerMenu
from iterator.menus.PancakeHouseMenu import PancakeHouseMenu
from iterator.iterators import Iterator


class Waitress:
    """ Implements the Waitress class specified by the example in the book """

    def __init__(self):
        """ Initialize with two menus: PancakeHouseMenu and DinerMenu """
        self.pancake_house_menu = PancakeHouseMenu()
        self.diner_menu = DinerMenu()

    def print_menu(self):
        """ Print the entire menu """
        pancake_iterator = self.pancake_house_menu.create_iterator()
        diner_iterator = self.diner_menu.create_iterator()

        print("MENU\n-----")
        print("BREAKFAST")
        self.print_menu_iterator(pancake_iterator)
        print("\nLUNCH")
        self.print_menu_iterator(diner_iterator)

    @staticmethod
    def print_menu_iterator(iterator: Iterator):
        """ Print the menu from iterator """
        while iterator.has_next():
            menu_item = iterator.next()
            print(menu_item.get_name(), ',', menu_item.get_price(), " -- ", menu_item.get_description())