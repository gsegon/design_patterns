from unittest import TestCase
from composite.components.Menu import Menu
from composite.components.MenuItem import MenuItem


class TestMenu(TestCase):

    def setUp(self) -> None:
        self.description = 'This is a description of some Menu'
        self.name = 'Name of the Menu'
        self.menu = Menu(self.name, self.description)

        self.menu_items = [MenuItem('Gulash', 'Hungarian stew dish', False, 2.35),
                           MenuItem('Wiener Schnitzel', 'Austrian specialty', False, 5.35),
                           MenuItem('Espresso', 'Espresso caffee', False, 2.50)]

    def test_add(self):
        self.menu.add(self.menu_items[0])
        self.assertTrue(self.menu_items[0] in self.menu.menu_components)

    def test_remove(self):
        self.menu.add(self.menu_items[0])
        self.menu.remove(self.menu_items[0])
        self.assertFalse(self.menu_items[0] in self.menu.menu_components)

    def test_get_child(self):
        self.menu.add(self.menu_items[0])
        item = self.menu.get_child(0)
        self.assertTrue(self.menu_items[0] is item)

    def test_get_description(self):
        print(self.menu.get_description())

    def test_print_menu(self):
        for item in self.menu_items:
            self.menu.add(item)

        print(self.menu)
