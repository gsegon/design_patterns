from unittest import TestCase

from strategy.clients.DecoyDuck import DecoyDuck

from strategy.behaviours.FlyWithWings import FlyWithWings


class TestDecoyDuck(TestCase):

    def setUp(self) -> None:
        self.duck = DecoyDuck()

    def test_display(self):
        self.duck.display()
        self.assertTrue(True)

    def test_quack(self):
        self.duck.perform_quack()
        self.assertTrue(True)

    def test_fly(self):
        self.duck.perform_fly()
        self.assertTrue(True)

    def test_change_fly_behaviour(self):
        self.duck.set_fly_behaviour(FlyWithWings())