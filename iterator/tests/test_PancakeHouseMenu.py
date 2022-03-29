from unittest import TestCase
from iterator.menus.PancakeHouseMenu import PancakeHouseMenu


class TestPancakeHouseMenu(TestCase):

    def setUp(self) -> None:
        self.menu = PancakeHouseMenu()

    def test_get_menu_items(self):
        menu_iterator = self.menu.create_iterator()

        while menu_iterator.has_next():
            item = menu_iterator.next()
            print('item: ', item)
