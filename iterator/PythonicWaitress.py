from iterator.menus.PythonicDinerMenu import PythonicDinerMenu
from iterator.menus.PythonicPancakeHouseMenu import PythonicPancakeHouseMenu
from iterator.menus.PythonicCafeMenu import PythonicCafeMenu

from iterator.iterators import Iterator


class PythonicWaitress:
    """ Implements the Waitress class specified by the example in the book """

    def __init__(self, pancake_menu: PythonicPancakeHouseMenu, diner_menu: PythonicDinerMenu,
                 cafe_menu: PythonicCafeMenu):
        """ Initialize with two menus: PancakeHouseMenu and DinerMenu """
        self.pancake_house_menu = pancake_menu
        self.diner_menu = diner_menu
        self.cafe_menu = cafe_menu

    def print_menu(self):
        """ Print the entire menu """
        pancake_iterator = self.pancake_house_menu.create_iterator()
        diner_iterator = self.diner_menu.create_iterator()
        cafe_iterator = self.cafe_menu.create_iterator()

        print("MENU\n-----")
        print("BREAKFAST")
        self.print_menu_iterator(pancake_iterator)
        print("\nLUNCH")
        self.print_menu_iterator(diner_iterator)
        print("\nDINNER")
        self.print_menu_iterator(cafe_iterator)

    @staticmethod
    def print_menu_iterator(iterator: Iterator):
        """ Print the menu from iterator """
        for menu_item in iterator:
            print(menu_item.get_name(), ',', menu_item.get_price(), " -- ", menu_item.get_description())