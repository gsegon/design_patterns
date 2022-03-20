from factory.stores.PizzaStore import PizzaStore
from factory.pizzas.Pizza import Pizza
from factory.pizzas.new_york.NYStyleCheesePizza import NYStyleCheesePizza
from factory.pizzas.new_york.NYStylePepperoniPizza import NYStylePepperoniPizza
from factory.pizzas.new_york.NYStyleClamPizza import NYStyleClamPizza
from factory.pizzas.new_york.NYStyleVeggiePizza import NYStyleVeggiePizza


class NYStylePizzaStore(PizzaStore):

    def create_pizza(self, pizza_type: str) -> Pizza:

        pizza = None

        if pizza_type == 'cheese':
            pizza = NYStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = NYStylePepperoniPizza()
        elif pizza_type == 'clam':
            pizza = NYStyleClamPizza()
        elif pizza_type == 'veggie':
            pizza = NYStyleVeggiePizza()

        return pizza
