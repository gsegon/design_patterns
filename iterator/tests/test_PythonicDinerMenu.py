from unittest import TestCase
from iterator.menus.PythonicDinerMenu import PythonicDinerMenu


class TestPythonicDinerMenu(TestCase):

    def setUp(self) -> None:
        self.menu = PythonicDinerMenu()

    def test_iterate(self):
        menu_iterator = self.menu.create_iterator()

        for item in menu_iterator:
            print('item: ', item)
