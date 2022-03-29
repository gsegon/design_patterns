from unittest import TestCase
from iterator.PythonicWaitress import PythonicWaitress


class TestPythonicWaitress(TestCase):

    def setUp(self) -> None:
        self.waitress = PythonicWaitress()

    def test_print_menu(self):
        self.waitress.print_menu()
