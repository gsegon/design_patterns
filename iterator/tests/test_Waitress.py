from unittest import TestCase
from iterator.Waitress import Waitress


class TestWaitress(TestCase):

    def setUp(self) -> None:
        self.waitress = Waitress()

    def test_print_menu(self):
        self.waitress.print_menu()
