from unittest import TestCase
from factory.abstract_factory.pizzas.CheesePizza import CheesePizza
from factory.abstract_factory.ingredients.NYPizzaIngredientFactory import NYPizzaIngredientFactory
from factory.abstract_factory.ingredients.ChicagoPizzaIngredientFactory import ChicagoPizzaIngredientFactory


class TestCheesePizza(TestCase):

    def setUp(self) -> None:
        self.ny_ingredients_factory = NYPizzaIngredientFactory()
        self.chicago_ingredients_factory = ChicagoPizzaIngredientFactory()

    def test_ny_cheese_pizza(self):
        self.pizza = CheesePizza(self.ny_ingredients_factory)
        self.pizza.prepare()

    def test_chicago_cheese_pizza(self):
        self.pizza = CheesePizza(self.chicago_ingredients_factory)
        self.pizza.prepare()

