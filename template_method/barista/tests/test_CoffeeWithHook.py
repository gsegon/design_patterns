from unittest import TestCase
from template_method.barista.CoffeeWithHook import CoffeeWithHook


class TestCoffeeWithHook(TestCase):

    def setUp(self) -> None:
        self.coffee = CoffeeWithHook()

    def test_prepare_recipe(self):
        self.coffee.prepare_recipe()