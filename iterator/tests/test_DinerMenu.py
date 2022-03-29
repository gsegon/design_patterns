from unittest import TestCase
from iterator.menus.DinerMenu import DinerMenu


class TestDinerMenu(TestCase):

    def setUp(self) -> None:
        self.menu = DinerMenu()

    def test_iterate(self):
        menu_iterator = self.menu.create_iterator()

        while menu_iterator.has_next():
            item = menu_iterator.next()
            print('item: ', item)
