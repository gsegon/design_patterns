from factory.abstract_factory.stores.PizzaStore import PizzaStore
from factory.abstract_factory.pizzas.Pizza import Pizza
from factory.abstract_factory.ingredients.ChicagoPizzaIngredientFactory import ChicagoPizzaIngredientFactory

from factory.abstract_factory.pizzas.CheesePizza import CheesePizza
from factory.abstract_factory.pizzas.ClamPizza import ClamPizza
from factory.abstract_factory.pizzas.VeggiePizza import VeggiePizza
from factory.abstract_factory.pizzas.PepperoniPizza import PepperoniPizza


class ChicagoPizzaStore(PizzaStore):

    def __init__(self):
        self.pizza = None
        self.ingredient_factory = ChicagoPizzaIngredientFactory()

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            self.pizza = CheesePizza(self.ingredient_factory)
            self.pizza.set_name('Chicago Style Cheese Pizza.')
        elif pizza_type == 'clams':
            self.pizza = ClamPizza(self.ingredient_factory)
            self.pizza.set_name('Chicago Style Clam Pizza.')
        elif pizza_type == 'veggie':
            self.pizza = VeggiePizza(self.ingredient_factory)
            self.pizza.set_name('Chicago Style Veggie Pizza.')
        elif pizza_type == 'pepperoni':
            self.pizza = PepperoniPizza(self.ingredient_factory)
            self.pizza.set_name('Chicago Style Pepperoni Pizza')

        return self.pizza
