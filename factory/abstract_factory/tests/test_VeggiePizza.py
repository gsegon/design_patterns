from unittest import TestCase
from factory.abstract_factory.pizzas.VeggiePizza import VeggiePizza
from factory.abstract_factory.ingredients.NYPizzaIngredientFactory import NYPizzaIngredientFactory
from factory.abstract_factory.ingredients.ChicagoPizzaIngredientFactory import ChicagoPizzaIngredientFactory


class TestVeggiePizza(TestCase):

    def setUp(self) -> None:
        self.ny_ingredients_factory = NYPizzaIngredientFactory()
        self.chicago_ingredients_factory = ChicagoPizzaIngredientFactory()

    def test_ny_clam_pizza(self):
        self.pizza = VeggiePizza(self.ny_ingredients_factory)
        self.pizza.prepare()

    def test_chicago_clam_pizza(self):
        self.pizza = VeggiePizza(self.chicago_ingredients_factory)
        self.pizza.prepare()

