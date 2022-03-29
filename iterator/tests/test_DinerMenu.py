from unittest import TestCase
from iterator.DinerMenu import DinerMenu


class TestDinerMenu(TestCase):

    def setUp(self) -> None:
        self.menu = DinerMenu()

    def test_get_menu_items(self):
        items = self.menu.get_menu_items()
        print(items)
