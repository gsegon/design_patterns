from unittest import TestCase
from factory.abstract_factory.pizzas.ClamPizza import ClamPizza
from factory.abstract_factory.ingredients.NYPizzaIngredientFactory import NYPizzaIngredientFactory
from factory.abstract_factory.ingredients.ChicagoPizzaIngredientFactory import ChicagoPizzaIngredientFactory


class TestClamPizza(TestCase):

    def setUp(self) -> None:
        self.ny_ingredients_factory = NYPizzaIngredientFactory()
        self.chicago_ingredients_factory = ChicagoPizzaIngredientFactory()

    def test_ny_clam_pizza(self):
        self.pizza = ClamPizza(self.ny_ingredients_factory)
        self.pizza.prepare()

    def test_chicago_clam_pizza(self):
        self.pizza = ClamPizza(self.chicago_ingredients_factory)
        self.pizza.prepare()

