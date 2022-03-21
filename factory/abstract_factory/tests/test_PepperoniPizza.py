from unittest import TestCase
from factory.abstract_factory.pizzas.PepperoniPizza import PepperoniPizza
from factory.abstract_factory.ingredients.NYPizzaIngredientFactory import NYPizzaIngredientFactory
from factory.abstract_factory.ingredients.ChicagoPizzaIngredientFactory import ChicagoPizzaIngredientFactory


class TestPepperoniPizza(TestCase):

    def setUp(self) -> None:
        self.ny_ingredients_factory = NYPizzaIngredientFactory()
        self.chicago_ingredients_factory = ChicagoPizzaIngredientFactory()

    def test_ny_pepperoni_pizza(self):
        self.pizza = PepperoniPizza(self.ny_ingredients_factory)
        self.pizza.prepare()

    def test_chicago_pepperoni_pizza(self):
        self.pizza = PepperoniPizza(self.chicago_ingredients_factory)
        self.pizza.prepare()

