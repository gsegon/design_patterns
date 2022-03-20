from factory.stores.PizzaStore import PizzaStore
from factory.pizzas.Pizza import Pizza
from factory.pizzas.chicago.ChicagoCheesePizza import ChicagoCheesePizza
from factory.pizzas.chicago.ChicagoPepperoniPizza import ChicagoPepperoniPizza
from factory.pizzas.chicago.ChicagoClamPizza import ChicagoClamPizza
from factory.pizzas.chicago.ChicagoVeggiePizza import ChicagoVeggiePizza


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, pizza_type: str) -> Pizza:

        pizza = None

        if pizza_type == 'cheese':
            pizza = ChicagoCheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = ChicagoPepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ChicagoClamPizza()
        elif pizza_type == 'veggie':
            pizza = ChicagoVeggiePizza()

        return pizza
