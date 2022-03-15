from unittest import TestCase

from strategy.clients.MallardDuck import MallardDuck


class TestRedheadDuck(TestCase):

    def setUp(self) -> None:
        self.duck = MallardDuck()

    def test_display(self):
        self.duck.display()
        self.assertTrue(True)

    def test_quack(self):
        self.duck.perform_quack()
        self.assertTrue(True)

    def test_fly(self):
        self.duck.perform_fly()
        self.assertTrue(True)
