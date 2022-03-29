from unittest import TestCase
from iterator.PancakeHouseMenu import PancakeHouseMenu


class TestPancakeHouseMenu(TestCase):

    def setUp(self) -> None:
        self.menu = PancakeHouseMenu()

    def test_get_menu_items(self):
        items = self.menu.get_menu_items()
        print(items)
