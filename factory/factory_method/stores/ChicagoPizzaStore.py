from factory.factory_method.stores.PizzaStore import PizzaStore
from factory.factory_method.pizzas import Pizza
from factory.factory_method.pizzas.chicago.ChicagoCheesePizza import ChicagoCheesePizza
from factory.factory_method.pizzas.chicago.ChicagoPepperoniPizza import ChicagoPepperoniPizza
from factory.factory_method.pizzas.chicago.ChicagoClamPizza import ChicagoClamPizza
from factory.factory_method.pizzas.chicago import ChicagoVeggiePizza


class ChicagoPizzaStore(PizzaStore):
    """ Classes that produce products are called concrete creators """

    def create_pizza(self, pizza_type: str) -> Pizza:
        """ This is our factory method implemented """

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
