from unittest import TestCase
from iterator.Waitress import Waitress
from iterator.menus.DinerMenu import DinerMenu
from iterator.menus.PancakeHouseMenu import PancakeHouseMenu
from iterator.menus.CafeMenu import CafeMenu


class TestWaitress(TestCase):

    def setUp(self) -> None:
        pancake_menu = PancakeHouseMenu()
        diner_menu = DinerMenu()
        cafe_menu = CafeMenu()

        self.waitress = Waitress(pancake_menu, diner_menu, cafe_menu)

    def test_print_menu(self):
        self.waitress.print_menu()
