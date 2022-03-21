from factory.abstract_factory.stores.PizzaStore import PizzaStore
from factory.abstract_factory.pizzas.Pizza import Pizza
from factory.abstract_factory.ingredients.NYPizzaIngredientFactory import NYPizzaIngredientFactory

from factory.abstract_factory.pizzas.CheesePizza import CheesePizza
from factory.abstract_factory.pizzas.ClamPizza import ClamPizza
from factory.abstract_factory.pizzas.VeggiePizza import VeggiePizza
from factory.abstract_factory.pizzas.PepperoniPizza import PepperoniPizza


class NYPizzaStore(PizzaStore):
    """ NYPizzaStore is the client code of pizzas. """

    def __init__(self):
        """ In the init function we choose which concrete factory we are using """
        self.pizza = None
        self.ingredient_factory = NYPizzaIngredientFactory()

    def create_pizza(self, pizza_type: str) -> Pizza:
        """ In create_pizza we call different pizza implementations by passing the concrete factory """

        if pizza_type == 'cheese':
            self.pizza = CheesePizza(self.ingredient_factory)
            self.pizza.set_name('NY Style Cheese Pizza.')
        elif pizza_type == 'clams':
            self.pizza = ClamPizza(self.ingredient_factory)
            self.pizza.set_name('NY Style Clam Pizza.')
        elif pizza_type == 'veggie':
            self.pizza = VeggiePizza(self.ingredient_factory)
            self.pizza.set_name('NY Style Veggie Pizza.')
        elif pizza_type == 'pepperoni':
            self.pizza = PepperoniPizza(self.ingredient_factory)
            self.pizza.set_name('NY Style Pepperoni Pizza')

        return self.pizza
