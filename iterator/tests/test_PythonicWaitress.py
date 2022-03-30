from unittest import TestCase
from iterator.PythonicWaitress import PythonicWaitress
from iterator.menus.PythonicDinerMenu import PythonicDinerMenu
from iterator.menus.PythonicPancakeHouseMenu import PythonicPancakeHouseMenu
from iterator.menus.PythonicCafeMenu import PythonicCafeMenu


class TestPythonicWaitress(TestCase):

    def setUp(self) -> None:
        pancake_menu = PythonicPancakeHouseMenu()
        diner_menu = PythonicDinerMenu()
        cafe_menu = PythonicCafeMenu()

        self.waitress = PythonicWaitress(pancake_menu, diner_menu, cafe_menu)

    def test_print_menu(self):
        self.waitress.print_menu()
