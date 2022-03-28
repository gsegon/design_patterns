from unittest import TestCase
from template_method.Coffee import Coffee


class TestCoffee(TestCase):

    def setUp(self) -> None:
        self.coffee = Coffee()

    def test_prepare_recipe(self):
        self.coffee.prepare_recipe()
