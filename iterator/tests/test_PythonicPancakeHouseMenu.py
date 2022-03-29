from unittest import TestCase
from iterator.menus.PythonicPancakeHouseMenu import PythonicPancakeHouseMenu


class TestPythonicPancakeHouseMenu(TestCase):

    def setUp(self) -> None:
        self.menu = PythonicPancakeHouseMenu()

    def test_iterate(self):
        menu_iterator = self.menu.create_iterator()

        for item in menu_iterator:
            print('item: ', item)
