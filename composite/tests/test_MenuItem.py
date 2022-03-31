from unittest import TestCase
from composite.components.MenuItem import MenuItem


class TestMenuItem(TestCase):

    def setUp(self) -> None:
        self.name = 'Name'
        self.description = 'Description blabla...'
        self.vegetarian = False
        self.price = 2.35
        self.menu_item = MenuItem(self.name, self.description, self.vegetarian, self.price)

    def test_get_name(self):
        self.assertEqual(self.menu_item.get_name(), self.name)

    def test_get_description(self):
        self.assertEqual(self.menu_item.get_description(), self.description)

    def test_get_price(self):
        self.assertEqual(self.menu_item.get_price(), self.price)

    def test_is_vegetarian(self):
        self.assertEqual(self.menu_item.is_vegetarian(), self.vegetarian)

    def test_print_menu_item(self):
        print(self.menu_item)