from unittest import TestCase
from factory.abstract_factory.ingredients.NYPizzaIngredientFactory import NYPizzaIngredientFactory


class TestNYPizzaIngredientFactory(TestCase):

    def setUp(self) -> None:
        self.ingredient_factory = NYPizzaIngredientFactory()

    def test_create_dough(self):
        self.ingredient_factory.create_dough()

    def test_create_sauce(self):
        self.ingredient_factory.create_sauce()

    def test_create_clams(self):
        self.ingredient_factory.create_clams()

    def test_create_cheese(self):
        self.ingredient_factory.create_cheese()

    def test_create_veggies(self):
        self.ingredient_factory.create_veggies()

