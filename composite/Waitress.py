from composite.components.Menu import Menu


class Waitress:
    """ Implements the Waitress class specified by the example in the book (Composite pattern)"""

    def __init__(self, all_menus: Menu):
        """ Initialize with two menus: PancakeHouseMenu and DinerMenu """
        self.all_menus = all_menus

    def print_menu(self):
        """ Print the entire menu """
        print(self.all_menus)
